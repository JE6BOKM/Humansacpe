from rest_framework.routers import DefaultRouter

from apps.humanscape.views import ClinicalInfoViewset, RecentlyUpdateListView

app_name = "humansacpe"

router = DefaultRouter()
router.register(r"latest", RecentlyUpdateListView)
router.register(r"detail", ClinicalInfoViewset)

urlpatterns = router.urls
