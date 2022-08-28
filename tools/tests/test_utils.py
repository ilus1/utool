import pytest
from tools.utils import ToolsUtils
from pytest_mock import MockerFixture
from datetime import datetime

class TestUtils:
    def test_count_day(self, mocker: MockerFixture):
        mocker.patch(
            'tools.utils.datetime'
        ).today.return_value=datetime(2022, 8, 28, 10, 9, 28, 688746)
        date1 = datetime(2022, 8, 26, 10, 9, 28, 688746)
        date2 = datetime(2022, 8, 28, 10, 9, 28, 688746)
        tools_utils = ToolsUtils()
        dias1 = tools_utils.count_days(date1, 2)
        dias2 = tools_utils.count_days(date1, 1)
        dias3 = tools_utils.count_days(date2, 6)
        assert dias1 == 0
        assert dias2 == 1
        assert dias3 == 6

