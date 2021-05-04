from django.urls import path

from .views import NewToolView

app_name = "tools"

urlpatterns = [
    path("", NewToolView.as_view(), name="new_tool")
]
