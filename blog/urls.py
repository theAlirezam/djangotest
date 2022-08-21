from blog.views import show_detail, show_archive
import re
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('detail/', show_detail),
    path('detail/<int:year>', show_archive),
    path('detail/<int:year>/<int:month>', show_archive),
    re_path(r'archive/(?P<code>[0-9]{4})/', show_archive),
    re_path(r'archive/(?P<code>\d{4})/', show_archive),


]

