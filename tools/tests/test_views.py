import pytest

from django.urls import resolve, reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser 

from ..models import Tool
from ..views import UserToolsListView
from users.models import MyUserModel

from .factories import ToolFactory, UserFactory

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

class TestUserToolsListView:
    def setup(self):
        self.factory = RequestFactory()
        self.user = UserFactory(
            username="test_user",
            email="teste_user@mail.com",
            password="test_password",
        )
        self.tool = ToolFactory(owner=self.user, is_available=True)
    
    def test_reverse_resolve(self):
        assert reverse("pages:my_tools") == "/my_tools/"
        assert resolve("/my_tools/").view_name == "pages:my_tools"

    def test_status_code_with_valid_user(self):
        request = self.factory.get("/my_tools/")
        request.user = self.user
        response = UserToolsListView.as_view()(request)
        
        assert response.status_code == 200
        assert response.template_name[0] == "tools/my_tools.html"

    def test_status_code_with_anonymous_user(self):
        request = self.factory.get("/my_tools/")
        request.user = AnonymousUser()
        response = UserToolsListView.as_view()(request)
        
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/my_tools/"

    def test_user_number_of_tools(self):
        request = self.factory.get("/my_tools/")
        request.user = self.user
        response = UserToolsListView.as_view()(request)
        
        assert response.context_data["object_list"].count() == 1
        assert response.context_data["object_list"][0] == self.tool
