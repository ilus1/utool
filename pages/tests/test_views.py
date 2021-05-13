import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed
from django.test import RequestFactory

@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass

@pytest.fixture

def home_response(client):
    return RequestFactory.get(client, path="/")

@pytest.fixture

def about_response(client):
    return RequestFactory.get(client, path="/about/")

class TestHomePageView:
    def test_reverse_resolve(self):
        assert reverse("pages:list") == "/"
        assert resolve("/").view_name == "pages:list"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "tools/tool_list.html")

""" class TestAboutView:
    def test_reverse_resolve(self):
        assert reverse("pages:about") == "/about/"
        assert resolve("/about/").view_name == "pages:about"

    def test_status_code(self, about_response):
        assert about_response.status_code == 200

    def test_template(self, about_response):
        assertTemplateUsed(about_response, "about.html") """