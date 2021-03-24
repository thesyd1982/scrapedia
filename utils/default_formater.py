from utils.i_formating import IFormating


class DefaultFormater(IFormating):
    def format_str(self, key, value):
        return f'\t{key}: {value}'


pass
