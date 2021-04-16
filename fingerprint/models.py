import json

from django.db import models

# Create your models here.
from django.http import QueryDict
from loguru import logger


class Fingerprint(models.Model):
    components = models.JSONField()
    hash = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def data_to_fingerprint(fingerprint_data: QueryDict) -> 'Fingerprint':
        hash = fingerprint_data["hash"]

        try:
            fingerprint = Fingerprint.objects.get(hash=hash)
            logger.debug(f"Fingerprint {hash} already exists")
        except models.ObjectDoesNotExist:
            components = json.loads(fingerprint_data["components"])
            logger.info(f"Found new fingerprint data: {components}")
            fingerprint = Fingerprint(components=components, hash=hash)
        fingerprint.save()
        return fingerprint

    def __str__(self):
        return f"<Fingerprint - {self.hash}>"
