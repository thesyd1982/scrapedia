from utils.formater.formatings.abstarct_formating import AbstarctFormating



class JsonFormating(AbstarctFormating):
    def format_string(self, dictionary, classename, excludes):

        """
            Parse str to Json Format
            :return: string representation of the obj on json format
        """

        f = classename.split('.')[1].replace("'>", '') + ' : \n'
        for key, value in self.__dict__.items():
            if key not in excludes:
                f += f'\t{key} : {str(value).rjust(3, "0")} ' + ' \n'
        f = "_" * 70 + "\n" + f + "\n" + "-" * 70
        return f

    # TODO Amelioration creation du decorateur pour chaque chaine de caracters
