class Parent:
    def __init__(self, parent_param_1, parent_param_2):
        self.parent_param_1 = parent_param_1
        self.parent_param_2 = parent_param_2

    def parent_method(self, param1):
        raise Exception('err')
        return param1 ** param1 * self.parent_param_1
