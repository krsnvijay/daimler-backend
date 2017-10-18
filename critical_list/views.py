import openpyxl
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets

from critical_list.forms import UploadFileForm
from critical_list.models import Part
from critical_list.serailizers import PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


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
