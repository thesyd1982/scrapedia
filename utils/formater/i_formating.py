from abc import ABC, abstractmethod


class IFormating(ABC):
    @abstractmethod
    def format_string(self, dictionary, classename, excludes):
        ...




