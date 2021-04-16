from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from loguru import logger

from fingerprint.models import Fingerprint
from fingerprint.serializers import FingerprintSerializer


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class ResultView(View):
    def get(self, request, hash_id=None, **kwargs):
        try:
            fp = Fingerprint.objects.get(hash=hash_id)
        except ObjectDoesNotExist:
            logger.info(f"Hash {hash_id} not found")
            return HttpResponseNotFound()

        serializer = FingerprintSerializer(fp)
        return JsonResponse(serializer.data)


class SaveFingerprintView(View):
    template_name = 'form_template.html'

    def post(self, request, *args, **kwargs):
        fp = Fingerprint.data_to_fingerprint(request.POST)
        fp.seen_counter += 1
        fp.save()
        return HttpResponse()
