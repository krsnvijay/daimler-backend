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
