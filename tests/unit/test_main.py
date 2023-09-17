from unittest.mock import MagicMock, patch, call
from copy import deepcopy

import pytest

from testing_class.main import call_if_f, call_for_f, call_return_value, call_side_effect, call_magick_mock_play,\
    call_sophisticated_mock, call_with_error, mocked_class


TEST_INPUT = '1'
TEST_IMAGINARY_DATA = ['item_1', 'item_2', 'item_3']
TEST_EXPECTED_DATA = ['modified_item_1', 'modified_item_2', 'modified_item_3']


@pytest.mark.skip
def test_skip():
    raise Exception("This test should be skipped")


def test_call_if_f_positive(common_data):
    input_pram = '1'
    actual = call_if_f(input_pram)
    expected = 'you in if'
    assert actual == expected


def test_call_if_f_negative(obj):
    input_pram = '2'
    actual = call_if_f(input_pram)
    expected = 'you out of if'
    assert actual == expected


@pytest.mark.parametrize('input_param, expected', [('1', 'you in if'), ('2', 'you out of if')])
def test_call_if_f(input_param, expected):
    actual = call_if_f(input_param)
    assert actual == expected


@patch('testing_class.main.call_if_f')
def test_call_for_f(mock_f):
    actual = call_for_f(deepcopy(TEST_IMAGINARY_DATA))
    expected_data = ['modified_item_1', 'modified_item_2', 'modified_item_3']
    assert actual == expected_data


# def test_call_for_f_2():
#     with patch('testing_class.main.call_if_f'):
#         actual = call_for_f(TEST_IMAGINARY_DATA)
#         expected_data = ['modified_item_1', 'modified_item_2', 'modified_item_3']
#         assert actual == expected_data


@patch('testing_class.main.call_if_f')
def test_call_return_value_1(mock_f):
    mock_f.return_value = ['mock_1', 'mock_2', 'mock_3']
    actual = call_return_value()
    expected_data = ['modified_mock_1', 'modified_mock_2', 'modified_mock_3']
    assert actual == expected_data

#
# @patch('testing_class.main.call_if_f', return_value=['mock_1', 'mock_2', 'mock_3'])
# def test_call_return_value_2(mock_f):
#     actual = call_return_value()
#     expected_data = ['modified_mock_1', 'modified_mock_2', 'modified_mock_3']
#     assert actual == expected_data
#
#
# def test_call_return_value_3():
#     with patch('testing_class.main.call_if_f', return_value=['mock_1', 'mock_2', 'mock_3']):
#         actual = call_return_value()
#         expected_data = ['modified_mock_1', 'modified_mock_2', 'modified_mock_3']
#         assert actual == expected_data
#
#
# def test_call_return_value_4():
#     with patch('testing_class.main.call_if_f') as mock_f:
#         mock_f.return_value = ['mock_1', 'mock_2', 'mock_3']
#         actual = call_return_value()
#         expected_data = ['modified_mock_1', 'modified_mock_2', 'modified_mock_3']
#         assert actual == expected_data


def return_param(param):
    return param


@patch('testing_class.main.call_if_f_modified', side_effect=return_param)
def test_call_side_effect(mock_f):
    input_data = deepcopy(TEST_IMAGINARY_DATA)
    actual = call_side_effect(input_data)
    expected_data = ['modified_item_1', 'item_2', 'item_3']
    assert actual == expected_data


@patch('testing_class.main.call_if_f_modified', side_effect=['mock_1', 'mock_2', 'mock_3'])
def test_call_side_effect_2(mock_f):
    input_data = deepcopy(TEST_IMAGINARY_DATA)
    actual = call_side_effect(input_data)
    expected_data = ['modified_mock_1', 'mock_2', 'mock_3']
    assert actual == expected_data


@patch('testing_class.main.call_if_f')
def test_call_magick_mock_play(mock_f):
    # x = MagicMock()
    call_magick_mock_play()
    mock_f.assert_called_once()
    print(mock_f.mock_calls)
 #    expected = [call('2'),
 # call().do_sheet(),
 # call().do_another_sheet(),
 # call().do_csv(),
 # call().do_csv().do_ololo()]
 #    assert expected == mock_f.mock_calls


@patch('testing_class.main.call_if_f')
def test_call_sophisticated_mock(mock_f):
    mock_f.return_value.call_another.return_value.call_third.return_value = ['mock_1', 'mock_2', 'mock_3']
    actual = call_sophisticated_mock()
    expected_data = ['modified_mock_1', 'modified_mock_2', 'modified_mock_3']
    assert actual == expected_data


def test_mocked_class():
    # kwargs = {'field': 10, 'method.return_value': 'configured'}
    # mock_inp = MagicMock()
    # mock_inp.configure_mock(**kwargs)

    # mock_inp = MagicMock(**kwargs)

    mock_inp = MagicMock()
    mock_inp.method.return_value = ['mock_1', 'mock_2', 'mock_3']
    mock_inp.field = 10
    mocked_class(mock_inp)

    # assert False


def test_call_with_error_valid():
    actual = call_with_error(10, 0)
    expected = 5
    assert actual == expected


def test_call_with_error_invalid():
    with pytest.raises(ZeroDivisionError):
        call_with_error(3, 0)
