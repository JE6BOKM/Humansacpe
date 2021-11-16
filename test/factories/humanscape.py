from datetime import timezone

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from faker import Faker

from apps.humanscape.models import ClinicalInfo

__all__ = ["ClinicalInfoFactory"]

fake = Faker()


class ClinicalInfoFactory(DjangoModelFactory):
    project_number = factory.fuzzy.FuzzyText(length=10)
    project_name = factory.fuzzy.FuzzyText(length=500)
    department = factory.fuzzy.FuzzyText(length=80)
    responsible_institution = factory.fuzzy.FuzzyText(length=120)
    total_target_number = factory.fuzzy.FuzzyInteger(fake.random_int())
    research_duration = factory.fuzzy.FuzzyText(length=10)
    research_type = factory.fuzzy.FuzzyText(length=10)
    clinical_trial_stage = factory.fuzzy.FuzzyText(length=20)
    research_scope = factory.fuzzy.FuzzyText(length=10)
    created_at = factory.fuzzy.FuzzyDateTime(fake.date_time(tzinfo=timezone.utc))
    updated_at = factory.fuzzy.FuzzyDateTime(fake.date_time(tzinfo=timezone.utc))

    class Meta:
        model = ClinicalInfo
        django_get_or_create = ["project_number"]

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        created_at = kwargs.pop("created_at", None)
        updated_at = kwargs.pop("updated_at", None)
        obj = super(ClinicalInfoFactory, cls)._create(target_class, *args, **kwargs)
        obj.created_at = created_at
        obj.updated_at = updated_at
        obj.save()
        return obj
