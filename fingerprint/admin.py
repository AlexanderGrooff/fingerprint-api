import json

from django.contrib import admin
from django.db.models import JSONField

from django.forms import widgets
from django_json_widget.widgets import JSONEditorWidget
from loguru import logger

from fingerprint.models import Fingerprint


class PrettyJSONWidget(widgets.Textarea):

    def format_value(self, value):
        try:
            value = json.dumps(json.loads(value), indent=2, sort_keys=True)
            # these lines will try to adjust size of TextArea to fit to content
            row_lengths = [len(r) for r in value.split('\n')]
            self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
            self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
            return value
        except Exception as e:
            logger.warning("Error while formatting JSON: {}".format(e))
            return super(PrettyJSONWidget, self).format_value(value)


@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    fields = ('hash', 'created', 'updated', 'seen_counter', 'components')
    readonly_fields = ('hash', 'created', 'updated', 'seen_counter')
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
