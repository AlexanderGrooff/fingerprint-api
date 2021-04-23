import json
from collections import defaultdict
from copy import copy
from typing import List

from django.db import models

# Create your models here.
from django.http import QueryDict
from loguru import logger


class Fingerprint(models.Model):
    components = models.JSONField()
    hash = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seen_counter = models.IntegerField(default=0)

    @staticmethod
    def data_to_fingerprint(fingerprint_data: QueryDict) -> "Fingerprint":
        hash = fingerprint_data["hash"]

        try:
            fingerprint = Fingerprint.objects.get(hash=hash)
            logger.debug(f"Fingerprint {hash} already exists")
        except models.ObjectDoesNotExist:
            components = json.loads(fingerprint_data["components"])
            logger.info(f"Found new fingerprint: {hash}")
            fingerprint = Fingerprint(components=components, hash=hash)
        return fingerprint

    @property
    def browser_name(self):
        values = self.components.get("vendorFlavors", {}).get("value")
        if values:
            return values[0]
        return "N/A"

    def __str__(self):
        return self.hash

    def _diff_to_fp(self, other_fp):
        fp_diff = {}
        for key in self.components.keys():
            fp1_v = copy(self.components[key])
            fp2_v = copy(other_fp.components[key])

            if isinstance(fp1_v, dict) and isinstance(fp2_v, dict):
                if "value" in fp1_v and "value" in fp2_v:
                    fp1_v = fp1_v["value"]
                    fp2_v = fp2_v["value"]

                elif "duration" in fp1_v and "duration" in fp2_v:
                    del fp1_v["duration"]
                    del fp2_v["duration"]

            if fp1_v != fp2_v:
                fp_diff[key] = {self: fp1_v, other_fp: fp2_v}
        return fp_diff

    def diff(self, *other_fps: List["Fingerprint"]):
        total_diff = defaultdict(dict)
        for other_fp in other_fps:
            logger.debug(f"Comparing {self} to {other_fp}")
            fp_diff = self._diff_to_fp(other_fp)
            for key in fp_diff:
                total_diff[key].update(fp_diff[key])
        return total_diff
