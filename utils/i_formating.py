from abc import ABC, abstractmethod


class IFormating(ABC):
    @abstractmethod
    def format_str(self, key, value):
        ...


pass





