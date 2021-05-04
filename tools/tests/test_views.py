import pytest
from django.urls import resolve, reverse

from .factories import ToolFactory

pytestmark = pytest.mark.django_db

class TestToolListView:
    def test_reverse_resolve(self):
        assert reverse("pages:list") == "/"
        assert resolve("/").view_name == "pages:list"

        url = reverse("pages:list_by_category", kwargs={"slug": "test-slug"})
        assert url == "/category/test-slug/"

        view_name = resolve("/category/test-slug/").view_name
        assert view_name == "pages:list_by_category"

    def test_status_code(self, client, category):
        response = client.get(reverse("pages:list"))
        assert response.status_code == 200

        response = client.get(
            reverse("pages:list_by_category", kwargs={"slug": category.slug})
        )
        assert response.status_code == 200

class TestToolDetailView:
    def test_reverse_resolve(self, tool):
        url = reverse("pages:detail", kwargs={"slug": tool.slug})
        assert url == f"/{tool.slug}/"

        view_name = resolve(f"/{tool.slug}/").view_name
        assert view_name == "pages:detail"

    def test_status_code(self, client):
        tool = ToolFactory(is_available=True)
        url = reverse("pages:detail", kwargs={"slug": tool.slug})
        response = client.get(url)
        assert response.status_code == 200