from django.urls import path

from .views import AboutPageView
from tools.views import NewToolView, ToolDetailView, ToolListView, DeleteToolView

app_name = "pages"

urlpatterns = [
    path("<slug:slug>/delete_tool/", DeleteToolView.as_view(), name="delete_tool"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", ToolListView.as_view(), name="list"),
    path("<slug:slug>/", ToolDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ToolListView.as_view(), name="list_by_category"),
]