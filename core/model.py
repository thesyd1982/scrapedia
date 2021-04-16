from utils.formater.formater import Formater
import uuid
from datetime import datetime

class Model:
    def __init__(self):
        id_model = 'id_'+self.get_classname().lower()
        uid = uuid.uuid4().__str__()
        self.__dict__[id_model] = uid
        self.creation_date = datetime.now()
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
