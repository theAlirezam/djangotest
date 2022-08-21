from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def show_detail(request):
    return HttpResponse('hi this is some details')


def show_archive(request, year=None, month=None):
    if year and month is not None:
        return HttpResponse(f'hi this is some archive from {year} / {month}')

    if year is not None:
        return HttpResponse(f'hi this is some archive from {year}')

