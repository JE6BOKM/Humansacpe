from django.urls import path

from apps.humanscape.views import ClinicalInfoViewset, RecentlyUpdateListView

app_name = "humanscape"

urlpatterns = [
    path("humanscape/<str:pk>/", ClinicalInfoViewset.as_view()),
    path("humanscape/latest/", RecentlyUpdateListView.as_view()),
]
