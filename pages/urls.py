from django.urls import path

from .views import AboutPageView
from tools.views import NewToolView, ToolDetailView, ToolListView

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", ToolListView.as_view(), name="list"),
    path("<slug:slug>/", ToolDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ToolListView.as_view(), name="list_by_category"),
]