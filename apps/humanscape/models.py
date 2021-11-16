from django.db import models


class ClinicalInfo(models.Model):
    """
    # project_number            과제번호	            string
    # project_name              과제명	                string
    # department                진료과	                string
    # responsible_institution   연구책임기관	        string
    # total_target_number       전체목표연구대상자수	int
    # research_duration         연구기간	            datetime
    # research_type             연구종류	            string
    # clinical_trial_stage      임상시험단계(연구모형)	string
    # research_scope            연구범위	            string
    # created_at                최초 업로드             datetime
    # updated_at                업데이트 시각           datetime
    """

    project_number = models.CharField(max_length=10, primary_key=True)
    project_name = models.CharField(max_length=500)
    department = models.CharField(max_length=80)
    responsible_institution = models.CharField(max_length=120)
    total_target_number = models.IntegerField(null=True)
    research_duration = models.CharField(max_length=20, null=True, blank=True)
    research_type = models.CharField(max_length=10)
    clinical_trial_stage = models.CharField(max_length=20, null=True)
    research_scope = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "clinical_infos"
