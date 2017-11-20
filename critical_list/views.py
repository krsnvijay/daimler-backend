import datetime

import openpyxl
from django.http import JsonResponse, Http404
from django.shortcuts import render
# Create your views here.
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from critical_list.forms import UploadFileForm
from critical_list.models import Part
from critical_list.permissions import IsManagerOrReadOnly
from critical_list.serailizers import PartSerializer


def get_starred_parts(request):
    user = request.user
    return user.starred_parts.all()


class PartFilter(filters.FilterSet):
    daterange = filters.DateFromToRangeFilter(name="short_on")

    class Meta:
        model = Part
        fields = ['shop', 'status', 'daterange', 'short_on']


class PartViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, DjangoModelPermissions]
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    search_fields = ('part_number',)
    ordering_fields = ('shop', 'short_on', 'status')
    filter_class = PartFilter

def convertToDB(records):

    for record in records:
        entry = Part()
        entry.part_number = record['part_number']
        entry.description = record['description']
        entry.supplier_name = record['supplier_name']
        entry.variants = record['variants']
        # entry.count = record['count']
        entry.reported_on = record['reported_on']
        entry.short_on = record['short_on']
        entry.shop = record['shop']
        entry.pmc = record['pmc']
        entry.team = record['team']
        entry.backlog = record['backlog']
        entry.region = record['region']
        entry.unloading_point = record['unloading_point']
        entry.p_q = record['p_q']
        entry.quantity = record['quantity']
        entry.quantity_expected = record['quantity_expected']
        entry.planned_vehicle_qty = record['planned_vehicle_qty']
        entry.eta_dicv = record['eta_dicv']
        entry.truck_details = record['truck_details']
        entry.shortage_reason = record['shortage_reason']
        entry.status = record['status']
        entry.save()

def handle_uploaded_file(f):
    wb = openpyxl.load_workbook(f)
    ws = wb['Dataset']

    part_list = []
    for row in range(3, ws.max_row + 1):
        x = {}
        if ws['A' + str(row)].font.color == "#110000" or ws['A' + str(row)].font.color == "#100":
            x['status'] = 3
        elif ws['A' + str(row)].font.color == "#111100" or ws['A' + str(row)].font.color == "#110":
            x['status'] = 2
        else:
            x['status'] = 1
        
        x['reported_on'] = ws['B' + str(row)].value
        x['short_on'] = ws['C' + str(row)].value
        x['shop'] = ws['D' + str(row)].value
        print(ws['D' + str(row)].value)
        x['variants'] = ws['E' + str(row)].value
        # x['count'] = ws['' + str(row)].value
        x['part_number'] = ws['G' + str(row)].value
        x['description'] = ws['H' + str(row)].value
        x['supplier_name'] = ws['I' + str(row)].value
        x['pmc'] = ws['J' + str(row)].value
        x['team'] = ws['K' + str(row)].value
        x['backlog'] = ws['N' + str(row)].value
        x['region'] = ws['P' + str(row)].value
        x['unloading_point'] = ws['Q' + str(row)].value
        x['p_q'] = ws['R' + str(row)].value
        x['quantity'] = ws['S' + str(row)].value
        x['quantity_expected'] = ws['T' + str(row)].value
        x['planned_vehicle_qty'] = ws['U' + str(row)].value
        x['eta_dicv'] = ws['V' + str(row)].value
        x['truck_details'] = ws['W' + str(row)].value
        x['shortage_reason'] = ws['X' + str(row)].value
                
        part_list.append(x)

    # convertToDB(part_list)
    return part_list

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return JsonResponse(handle_uploaded_file(request.FILES['file']), safe=False)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


class PartStatusChangeViewSet(APIView):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, IsManagerOrReadOnly]

    def patch(self, request, pk, format=None):
        try:
            obj = Part.objects.get(pk=pk)
            serializer = PartSerializer(obj, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Part.DoesNotExist:
            raise Http404


class CriticalListViewSet(APIView):
    """
    get: Get Shoptypes and their part info
    """
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]

    def get(self, request, format=None):
        shopvalues = 'MDT ENGINE', 'HDT ENGINE', 'TRANSMISSION', 'CASTING AND FORGING', 'AXLE'
        q = Part.objects.all()
        date = datetime.datetime.today()
        x = {}
        x['total'] = q.filter(short_on=date).count()
        x['critical'] = q.filter(short_on=date, status=3).count()
        x['warning'] = q.filter(short_on=date, status=2).count()
        x['normal'] = q.filter(short_on=date, status=1).count()
        for shop in shopvalues:
            x[shop] = {}
            o = {}
            o['total'] = q.filter(short_on=date, shop=shop).count()
            o['critical'] = q.filter(short_on=date, shop=shop, status=3).count()
            o['warning'] = q.filter(short_on=date, shop=shop, status=2).count()
            o['normal'] = q.filter(short_on=date, shop=shop, status=1).count()
            x[shop] = o
        return Response(x)
