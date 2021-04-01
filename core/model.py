from utils.formater.formater import Formater


class Model:
    def __init__(self):
        self.formater = Formater()

    def __str__(self):
        return self.formater.format_string(self.__dict__, self.get_classname(), ['formater'])

    def set_formating(self, formating):
        self.formater.formating = formating
        return self

    def get_obj(self):
        return self

    @classmethod
    def get_classname(cls):
        return cls.__name__
