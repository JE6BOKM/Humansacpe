from datetime import timedelta

from django.utils import timezone

import django_filters

from apps.humanscape.models import ClinicalInfo


class ClinialInfoRecentlyUpdateFilter(django_filters.FilterSet):
    week = django_filters.NumberFilter(
        field_name="updated_at", method="get_recently_update_week"
    )

    def get_recently_update_week(self, queryset, field_name):
        time = timezone.now() - timedelta(weeks=1)
        return queryset.filter(update_at__gte=time)

    class Meta:
        model = ClinicalInfo
        fields = ["week"]
