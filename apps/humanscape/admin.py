from django.contrib import admin

from apps.humanscape.models import ClinicalInfo


@admin.register(ClinicalInfo)
class ClinicalInfoAdmin(admin.ModelAdmin):
    """Clinical Information Admin"""

    list_display = (
        "project_number",
        "project_name",
        "department",
        "responsible_institution",
        "total_target_number",
        "research_duration",
        "research_type",
        "clinical_trial_stage",
        "research_scope",
        "created_at",
        "updated_at",
    )
