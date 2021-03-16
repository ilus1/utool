from django.urls import path

from .views import ToolDetailView, ToolListView

app_name = "tools"

urlpatterns = [
    path("", ToolListView.as_view(), name="list"),
    path("<slug:slug>/", ToolDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ToolListView.as_view(), name="list_by_category"),
]

