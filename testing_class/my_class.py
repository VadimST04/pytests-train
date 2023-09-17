from testing_class.parent import Parent


class MyClass(Parent):
    def __init__(self, parent_param_1, parent_param_2):
        super().__init__(parent_param_1, parent_param_2)
        self.field = 'field'

    def do_sheet(self):
        self.do_another_sheet()
        """some logic"""
        return None

    @staticmethod
    def do_another_sheet():
        raise Exception()

    def call_method(self):
        self.parent_method(None)
        self.do_sheet()
        self.do_another_sheet()
        """lots of logic below"""

