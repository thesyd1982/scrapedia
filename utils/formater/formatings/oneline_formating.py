from utils.formater.formatings.abstarct_formating import AbstarctFormating
from termcolor import colored


class OnelineFormating(AbstarctFormating):

    def __init__(self, excludes=[], displayclassname=True):
        super().__init__(excludes)
        self.displayclassname = displayclassname

    def format_string(self, dictionary, classename, excludes):
        f = ''
        excludes += self.excludes
        if self.displayclassname:
            f = colored(classename.capitalize() + ' : ', 'green')
        for key, value in dictionary.items():
            if key not in excludes:
                f += f'|  {key} : {str(value).rjust(3, "0")} ' + ' '
        f = self.put_delimiters(f, "\n", "")
        return f

    # TODO Amelioration creation du decorateur pour chaque chaine de caracters
    def put_delimiters(self, s, del1='', del2=''):
        return f'{del1}{s}{del2}'
