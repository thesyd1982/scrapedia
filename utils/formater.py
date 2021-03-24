from utils.default_formater import DefaultFormater
from abc import ABC


class Formater(ABC):

    def __init__(self):
        self.obj_formating = DefaultFormater()

    def __str__(self):
        return self.formating_str()

    def __repr__(self):
        f = '\t"' + self.classname() + '" : { \n '
        for key, value in self.__dict__.items():
            if key != 'obj_formating':
                f += '\t\t"' + str(key) + '" : "' + str(value) + '" ,\n'
        f = f[0:-2] + '\n\t}'
        f = self.put_delimiters(f, "{\n", "\n}")
        return f

    def formating_str(self):
        """
        format a dictionary
        :return: string representation of the obj
        """

        f = self.classname() + ' :\n'
        for key, value in self.__dict__.items():
            if key != 'obj_formating':
                f += DefaultFormater().format_str(key, value) + '\n'
        f = self.put_delimiters(f, "\n" + "#" * 50 + "\n", "#" * 50)
        return f

    def set_formating(self, obj):
        self.obj_formating = obj
        return self

    def classname(self):
        return str(self.__class__).split('.')[1].replace("'>", '')

    def put_delimiters(self, s, del1='', del2=''):
        return f'{del1}{s}{del2}'


pass
#
# print(colored('hello', 'red'), colored('world', 'green'))
