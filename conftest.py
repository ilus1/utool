import pytest

from tools.tests.factories import CategoryFactory, ToolFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def category():
    return CategoryFactory()

@pytest.fixture
def tool():
    return ToolFactory()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass