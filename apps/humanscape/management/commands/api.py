from django.conf import settings
from django.core.management.base import BaseCommand

import requests

from apps.humanscape.models import ClinicalInfo


def replace_duration(duration: str) -> str:
    """개월/년을 Month/Year로 변경해줌"""
    if len(duration) <= 1:
        return ""
    if "개월" in duration:
        months = duration.split("개월")[0]
        return f"{months} Months" if int(months) != 1 else f"{months} Month"
    if "년" in duration:
        years = duration.split("년")[0]
        return f"{years} Years" if int(years) != 1 else f"{years} Year"


def get_project_info(data: dict) -> dict:
    project = {}
    project["project_number"] = data.get("과제번호", "")
    project["project_name"] = data.get("과제명", "")
    project["department"] = data.get("진료과", "")
    project["responsible_institution"] = data.get("연구책임기관", "")
    project["total_target_number"] = (
        int(data.get("전체목표연구대상자수", 0)) if data.get("전체목표연구대상자수", 0) else None
    )
    project["research_duration"] = replace_duration(data.get("연구기간", ""))
    project["research_type"] = data.get("연구종류", "")
    project["clinical_trial_stage"] = data.get("임상시험단계(연구모형)", "")
    project["research_scope"] = data.get("연구범위", "")
    return project


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        secret_key = settings.DATA_SECRET_KEY
        url = f"https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?serviceKey={secret_key}"
        page = 1
        per_page = 20
        payload = {"page": page, "perPage": per_page}
        res = requests.get(url, params=payload)
        total_count = res.json().get("totalCount")
        max_page = (
            total_count // per_page
            if total_count % per_page == 0
            else (total_count // per_page) + 1
        )

        count = {"total": total_count, "created": 0, "updated": 0}
        for page in range(max_page):
            payload = {"page": page, "perPage": per_page}
            res = requests.get(url, params=payload)
            json_data = res.json()
            for data in json_data.get("data"):
                project = get_project_info(data)
                clinical_info = ClinicalInfo.objects.filter(
                    project_number=project.get("project_number")
                )
                if not clinical_info:
                    # 없는경우 object 생성
                    ClinicalInfo.objects.create(**project)
                    count["created"] += 1
                else:
                    # 있는경우 데이터 확인 후 업데이트
                    old_data = clinical_info.values().first()
                    old_data.pop("created_at")
                    old_data.pop("updated_at")
                    if old_data != project:
                        clinical_info.update(**project)
                        count["updated"] += 1
        self.stdout.write(
            self.style.SUCCESS(
                f"{count.get('created')} Info(s) Created.  "
                f"{count.get('updated')} Info(s) Updated.  "
                f"Total {count.get('total')} Infos saved."
            )
        )
