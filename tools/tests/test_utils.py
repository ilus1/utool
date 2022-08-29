import pytest
from tools.utils import ToolsUtils
from pytest_mock import MockerFixture
from datetime import datetime

class TestUtils:
    def test_count_day(self, mocker: MockerFixture):
        mocker.patch(
            'tools.utils.datetime'
        ).today.return_value=datetime(2022, 8, 28, 10, 9, 28, 688746)
        date = datetime(2022, 8, 26, 10, 9, 28, 688746)
        _date = datetime(2022, 8, 26, 10, 9, 28, 688746)
        _date_ = datetime(2022, 8, 22, 10, 9, 28, 688746)
        tools_utils = ToolsUtils()
        count = tools_utils.count_days(date, 2)
        _count = tools_utils.count_days(_date, 4)
        _count_ = tools_utils.count_days(_date_, 5)
        assert count ==  'Hoje é a data de devolução da ferramenta'
        assert _count ==  'A devolução é daqui a 2 dias'
        assert _count_ ==  'A devolução está atrasada 1 dia'