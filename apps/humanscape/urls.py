from django.urls import path

from apps.humanscape.views import ClinicalInfoViewset, RecentlyUpdateListView

app_name = "humanscape"

urlpatterns = [
    path("", ClinicalInfoViewset.as_view({"get": "list"})),
    path("<str:pk>/", ClinicalInfoViewset.as_view({"get": "retrieve"})),
    path("latest/", RecentlyUpdateListView.as_view({"get": "list"})),
]
