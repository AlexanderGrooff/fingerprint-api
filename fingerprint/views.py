import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from loguru import logger

from fingerprint.models import Fingerprint


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class SaveFingerprintView(View):
    template_name = 'form_template.html'

    def post(self, request, *args, **kwargs):
        fp = Fingerprint.data_to_fingerprint(request.POST)
        return HttpResponse()
