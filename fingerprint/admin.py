from django.contrib import admin
from django.db.models import JSONField

from django_json_widget.widgets import JSONEditorWidget

from fingerprint.models import Fingerprint


@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    fields = (
        "hash",
        "browser_name",
        "created",
        "updated",
        "seen_counter",
        "components",
    )
    readonly_fields = ("hash", "browser_name", "created", "updated", "seen_counter")
    list_display = ("hash", "browser_name", "created", "seen_counter")
    ordering = ("-created",)
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
