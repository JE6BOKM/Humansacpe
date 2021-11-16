from rest_framework.routers import DefaultRouter

from apps.humanscape.views import ClinicalInfoViewset, RecentlyUpdateListView

app_name = "humanscape"

router = DefaultRouter()
router.register(r"latest", RecentlyUpdateListView, basename="latest")
router.register(r"", ClinicalInfoViewset)


urlpatterns = router.urls
