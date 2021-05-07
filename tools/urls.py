from django.urls import path

from .views import ToolChoicesView, NewToolDisposablePartsView, NewToolView, NewToolWrenchView, NewToolEletricView

app_name = "tools"

urlpatterns = [
    path("", ToolChoicesView.as_view(), name="new_tool"),
    path("manual/", NewToolView.as_view(), name="new_tool_manual"),
    path("disposable_parts/", NewToolDisposablePartsView.as_view(), name="new_tool_disposable_part"),
    path("wrench/", NewToolWrenchView.as_view(), name="new_tool_wrench"),
    path("eletric/", NewToolEletricView.as_view(), name="new_tool_eletric"),
]
