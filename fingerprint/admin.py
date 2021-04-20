from django.contrib import admin
from django.db.models import JSONField
from django.db.models.query import QuerySet
from django.shortcuts import render

from django_json_widget.widgets import JSONEditorWidget

from fingerprint.models import Fingerprint


@admin.action(description="Find difference")
def find_diff(modeladmin, request, queryset: QuerySet[Fingerprint]):
    if queryset:
        diff = queryset[0].diff(*queryset)

        return render(
            request,
            "diff.html",
            context={"diff": sorted(diff.items()), "unique_fps": queryset.all()},
        )


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
    actions = [find_diff]
