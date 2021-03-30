from core.model import Model


class Provider(Model):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self


pass
