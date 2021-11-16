import pytest
from schema import Or, Schema


@pytest.fixture
def clinicalinfo_detail_schema():
    schema = Schema(
        {
            "project_number": str,
            "project_name": str,
            "department": str,
            "responsible_institution": str,
            "total_target_number": int,
            "research_duration": str,
            "research_type": str,
            "clinical_trial_stage": str,
            "research_scope": str,
            "created_at": str,
            "updated_at": str,
        }
    )
    return schema


@pytest.fixture
def clinicalinfo_list_schema(clinicalinfo_detail_schema):
    schema = Schema(
        {
            "count": int,
            "next": Or(str, None),
            "previous": Or(str, None),
            "results": [clinicalinfo_detail_schema],
        }
    )
    return schema
