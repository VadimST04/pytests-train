import logging

IMAGINARY_DATA = ['item_1', 'item_2', 'item_3']


def call_if_f(param_1):
    print('f 1')
    if param_1 == '1':
        return 'you in if'
    return 'you out of if'


def call_for_f(data):
    logging.info('f 2')
    call_if_f('2')
    for index, val in enumerate(data):
        data[index] = f'modified_{val}'
    return data


def call_return_value():
    data = call_if_f('2')
    for index, val in enumerate(data):
        data[index] = f'modified_{val}'
    return data


def call_if_f_modified(param_1):
    return f'I modify your param a lot {param_1}'


def call_side_effect(data):
    for index, val in enumerate(data):
        val = call_if_f_modified(val)
        if val.find('1') != -1:
            data[index] = f'modified_{val}'
        else:
            data[index] = val
    return data


def call_magick_mock_play():
    some_var = call_if_f('2')
    some_var.do_sheet()
    some_var.do_another_sheet()
    some_var.do_csv().do_ololo()


def call_sophisticated_mock():
    data = call_if_f('2').call_another().call_third()
    for index, val in enumerate(data):
        data[index] = f'modified_{val}'
    return data


def mocked_class(obj):
    print(obj.method())
    print(obj.f)
    print(obj.field)


def call_with_error(left, right):
    return left / (right + 1)


if __name__ == '__main__':
    call_if_f('1')
    main_data = call_for_f(IMAGINARY_DATA)
    modified_main_data = call_return_value()
    print(call_with_error(1, 3))
