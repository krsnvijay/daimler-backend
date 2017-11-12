import datetime

import openpyxl
from django.http import JsonResponse, Http404
from django.shortcuts import render
# Create your views here.
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from critical_list.forms import UploadFileForm
from critical_list.models import Part
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
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    search_fields = ('part_number',)
    ordering_fields = ('shop', 'short_on', 'status')
    filter_class = PartFilter

def handle_uploaded_file(f):
    wb = openpyxl.load_workbook(f)
    ws = wb.active

    part_list = []
    for row in range(2, ws.max_row + 1):
        x = {}
        if ws['A' + str(row)].font.color != None:
            x['delayed'] = True
        x['part_number'] = ws['A' + str(row)].value
        x['description'] = ws['B' + str(row)].value
        x['supplier_name'] = ws['C' + str(row)].value
        x['eta_dicv'] = ws['D' + str(row)].value
        x['truck_details'] = ws['E' + str(row)].value
        x['shortage_reason'] = ws['F' + str(row)].value
        x['shortage_reason'] = ws['F' + str(row)].value
        part_list.append(x)
    return part_list


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return JsonResponse(handle_uploaded_file(request.FILES['file']), safe=False)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


shopvalues = 'MDT ENGINE', 'HDT ENGINE', 'TRANSMISSION', 'CASTING AND FORGING', 'AXLE'


class CriticalListViewSet(APIView):
    """
    get: List all the critical list parts upto 3 days.
    """
    authentication_classes = (TokenAuthentication, OAuth2Authentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]

    def get(self, request, format=None):
        q = Part.objects.all()
        today = datetime.datetime.today()
        x = {}
        days = [today.strftime('%Y-%m-%d'), (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                (today + datetime.timedelta(days=2)).strftime('%Y-%m-%d')]

        for shop in shopvalues:
            x[shop] = {}
            for date in days:
                o = {}
                o['parts'] = PartSerializer(q.filter(short_on=date, shop=shop), many=True,
                                            context={'request': request}).data
                o['critical'] = q.filter(short_on=date, shop=shop, status=3).count()
                o['warning'] = q.filter(short_on=date, shop=shop, status=2).count()
                x[shop][date] = o
        return Response(x)


class CriticalDetailViewSet(APIView):
    """
    shop:'MDT ENGINE', 'HDT ENGINE', 'TRANSMISSION', 'CASTING AND FORGING', 'AXLE'
    get:Returns critical list of a particualr shop type
    """
    authentication_classes = (TokenAuthentication, OAuth2Authentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]

    def get(self, request, shop, format=None):
        query_set = Part.objects.all()
        today = datetime.datetime.today()
        print(shop)
        if shop in shopvalues:
            x = {}
            days = [today.strftime('%Y-%m-%d'), (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                    (today + datetime.timedelta(days=2)).strftime('%Y-%m-%d')]
            for date in days:
                o = {}
                o['parts'] = PartSerializer(query_set.filter(short_on=date, shop=shop), many=True,
                                            context={'request': request}).data
                o['critical'] = query_set.filter(short_on=date, shop=shop, status=3).count()
                o['warning'] = query_set.filter(short_on=date, shop=shop, status=2).count()
                x[date] = o

            return Response(x)
        else:
            raise Http404
