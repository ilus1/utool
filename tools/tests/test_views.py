import pytest
from django.urls import resolve, reverse

from .factories import ToolFactory

pytestmark = pytest.mark.django_db

class TestToolListView:
    def test_reverse_resolve(self):
        assert reverse("tools:list") == "/tools/"
        assert resolve("/tools/").view_name == "tools:list"

        url = reverse("tools:list_by_category", kwargs={"slug": "test-slug"})
        assert url == "/tools/category/test-slug/"

        view_name = resolve("/tools/category/test-slug/").view_name
        assert view_name == "tools:list_by_category"

    def test_status_code(self, client, category):
        response = client.get(reverse("tools:list"))
        assert response.status_code == 200

        response = client.get(
            reverse("tools:list_by_category", kwargs={"slug": category.slug})
        )
        assert response.status_code == 200

class TestToolDetailView:
    def test_reverse_resolve(self, tool):
        url = reverse("tools:detail", kwargs={"slug": tool.slug})
        assert url == f"/tools/{tool.slug}/"

        view_name = resolve(f"/tools/{tool.slug}/").view_name
        assert view_name == "tools:detail"

    def test_status_code(self, client):
        tool = ToolFactory(is_available=True)
        url = reverse("tools:detail", kwargs={"slug": tool.slug})
        response = client.get(url)
        assert response.status_code == 200