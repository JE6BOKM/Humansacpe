from datetime import timedelta

from django.utils import timezone

import pytest
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse

from apps.humanscape.models import ClinicalInfo
from test.factories import ClinicalInfoFactory

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_list_clinicalinfo(
        self,
        no_auth_client,
        clinicalinfo_list_schema,
    ):
        register_url = reverse("humanscape:api-root")

        resp = no_auth_client.get(register_url)
        assert resp.status_code == status.HTTP_200_OK
        assert clinicalinfo_list_schema.is_valid(resp.json())

    def test_detail_clinicalinfo(
        self,
        no_auth_client,
        clinicalinfo_detail_schema,
    ):
        ClinicalInfoFactory(project_number="C123")

        detail_url = reverse("humanscape:clinicalinfo-detail", kwargs={"pk": "C123"})

        resp = no_auth_client.get(detail_url)
        assert resp.status_code == status.HTTP_200_OK
        assert clinicalinfo_detail_schema.is_valid(resp.json())

        detail_url = reverse("humanscape:clinicalinfo-detail", kwargs={"pk": "xx"})

        resp = no_auth_client.get(detail_url)
        assert resp.status_code == status.HTTP_404_NOT_FOUND

    def test_search_clinicalinfo(
        self,
        no_auth_client,
        clinicalinfo_list_schema,
    ):
        ClinicalInfoFactory.create_batch(size=3)
        ClinicalInfoFactory(project_name="조직구증식증 임상연구 네트워크 구축 및 운영(HLH)")
        ClinicalInfoFactory(project_name="조직구증식증 임상연구 네트워크 구축 및 운영(LCM)")

        assert ClinicalInfo.objects.count() == 5

        list_url = reverse("humanscape:api-root")

        resp = no_auth_client.get(list_url, {"project_name": "조직"})
        result = resp.json()["results"]
        assert len(result) == 2
        assert resp.status_code == status.HTTP_200_OK
        assert clinicalinfo_list_schema.is_valid(resp.json())

    def test_latest_clinicalinfo(
        self,
        no_auth_client,
        clinicalinfo_list_schema,
    ):
        with freeze_time(timezone.localtime() - timedelta(weeks=2)):
            ClinicalInfoFactory.create_batch(size=20)

        with freeze_time(timezone.localtime()):
            ClinicalInfoFactory.create_batch(size=5)

        assert ClinicalInfo.objects.count() == 25

        latest_url = reverse("humanscape:latest-list")

        resp = no_auth_client.get(latest_url)
        result = resp.json()["results"]
        assert len(result) == 5
        assert resp.status_code == status.HTTP_200_OK
        assert clinicalinfo_list_schema.is_valid(resp.json())
