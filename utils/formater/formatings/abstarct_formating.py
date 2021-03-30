from abc import ABC

from utils.formater.i_formating import IFormating


class AbstarctFormating(IFormating, ABC):
    def __init__(self, excludes=[]):
        self.excludes = excludes
