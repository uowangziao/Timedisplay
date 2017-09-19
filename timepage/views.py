# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
  }
  return render(request,'timepage/index.html',context)
