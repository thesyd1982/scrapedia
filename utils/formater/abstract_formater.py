from abc import ABC


class AbstractFormater(ABC):

    def __init__(self):
        self.formating = None

    def format_string(self, dictionary, classename, excludes):
        return self.formating.format_string(dictionary, classename, excludes)

    def set_formating(self, obj):
        self.formating = obj


