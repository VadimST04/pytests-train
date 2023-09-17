from unittest.mock import patch
import pytest

from testing_class.my_class import MyClass
from testing_class.parent import Parent


@pytest.fixture()
def obj():
    return MyClass(None, None)


@patch('testing_class.my_class.MyClass.do_another_sheet', return_value='')
def test_do_sheet(common_data):
    obj.do_sheet()


@patch.object(MyClass, 'do_another_sheet', return_value='')
@patch.object(Parent, 'parent_method', return_value='')
def test_call_method(obj, mock_):
    obj.call_method()

# don't I remember the syntax
# @patch.multiple()