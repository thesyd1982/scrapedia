from utils.formater.abstract_formater import AbstractFormater
from utils.formater.formatings.default_formating import DefaultFormating



class Formater(AbstractFormater):
    def __init__(self):
        self.formating = DefaultFormating()

    def put_delimiters(self, s, del1='', del2=''):
        return f'{del1}{s}{del2}'
