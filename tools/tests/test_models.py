import pytest
from pytest_django.asserts import assertQuerysetEqual

from ..models import Tool
from .factories import ToolFactory

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test___str__(self, category):
        assert category.__str__() == category.name
        assert str(category) == category.name

    def test_get_absolute_url(self, category):
        url = category.get_absolute_url()
        assert url == f"/tools/category/{category.slug}/"


class TestToolModel:
    def test___str__(self, tool):
        assert tool.__str__() == tool.name
        assert str(tool) == tool.name

    def test_get_absolute_url(self, tool):
        url = tool.get_absolute_url()
        assert url == f"/tools/{tool.slug}/"

    def test_available_manager(self):
        ToolFactory(is_available=True)
        ToolFactory(is_available=False)

        assert Tool.objects.all().count() == 2
        assert Tool.available.all().count() == 1
        assertQuerysetEqual(
            Tool.available.all(),
            Tool.objects.filter(is_available=True),
            transform=lambda x: x,
        )