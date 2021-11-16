from rest_framework.routers import DefaultRouter

from apps.humanscape.views import ClinicalInfoViewset

app_name = "humanscape"

router = DefaultRouter()
router.register(r"trials", ClinicalInfoViewset())

urlpatterns = router.urls
