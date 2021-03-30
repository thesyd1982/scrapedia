from utils.formater.formatings.abstarct_formating import AbstarctFormating


class DefaultFormating(AbstarctFormating):

    def __init__(self, excludes=[]):
        super().__init__(excludes)

    def format_string(self, dictionary, classename, excludes):
        excludes += self.excludes
        """
            format a dictionary
            :return: string representation of the obj
        """

        f = "\n\t" + classename + ' : \n'

        for key, value in dictionary.items():
            if key not in excludes:
                f += f'\t {key} : \t {str(value)} ' + ' \n'
        f = self.put_delimiters(f, "_" * 70 + "\n", "-" * 70)
        return f

    def put_delimiters(self, s, del1='', del2=''):
        return f'{del1}{s}{del2}'
