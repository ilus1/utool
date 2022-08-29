from unittest import TestCase
import pytest
from pytest_django.asserts import assertQuerysetEqual
from ..models import Tool
from .factories import ToolFactory
from django.test.client import RequestFactory
from .tool_filters import ToolFilter

pytestmark = pytest.mark.django_db
class FiltersTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_ascending_a_first(self):
        self.tool = ToolFactory(
          name="A",
          price=10.0
        ), ToolFactory(
          name="B",
          price=20.0
        )
        request = self.factory.get("/my_tools/")
        request.tool = Tool.objects.all()
        ascending = ToolFilter.filter_by_order(
          self, request.tool, "", "ascending"
        )
        
        assertQuerysetEqual(
            ascending, request.tool,
            transform=lambda x: x,
        )

        a_first = ToolFilter.filter_by_order(
          self, request.tool, "", "a_first"
        )
        
        assertQuerysetEqual(
            a_first, request.tool,
            transform=lambda x: x,
        )

    def test_descending(self):
        self.tool = ToolFactory(
          name="A",
          price=20.0
        ), ToolFactory(
          name="B",
          price=10.0
        )
        request = self.factory.get("/my_tools/")
        request.tool = Tool.objects.all()
        descending = ToolFilter.filter_by_order(
          self, request.tool, "", "descending"
        )
        
        assertQuerysetEqual(
            descending, request.tool,
            transform=lambda x: x
        )