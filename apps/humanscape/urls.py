from rest_framework.routers import DefaultRouter

<<<<<<< HEAD
from apps.humanscape.views import ClinicalInfoViewset
=======
from apps.humanscape.views import RecentlyUpdateListView
>>>>>>> 59fbf06 (FEAT: Add Recently Update List API)

app_name = "humanscape"

router = DefaultRouter()
<<<<<<< HEAD
router.register(r"trials", ClinicalInfoViewset())
=======
router.register(r"humanscape", RecentlyUpdateListView)

>>>>>>> 59fbf06 (FEAT: Add Recently Update List API)

urlpatterns = router.urls
