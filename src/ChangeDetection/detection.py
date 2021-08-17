from abc import ABC, abstractmethod
from typing import List, Optional


class Detection(ABC):

    def __init__(self, old: Optional[str] = None, new: Optional[str] = None):
        self.changes = None
        if old is None:
            old = ""
        if new is not None:
            self.detect(old, new)

    def detect(self, old: str, new: str) -> List[str]:

        self.changes = self.__detect__(old, new)
        return self.changes

    @abstractmethod
    def __detect__(self, old: str, news: str) -> List[str]:
        pass

    def print(self, mode: Optional[str] = "color"):
        if not self.changes:
            return
        DEFAULT = '\033[m'
        GREEN = '\033[32m'
        RED = '\033[31m'

        for change in self.changes:
            key = change[0]
            value = change[1:]

            if key == "+":
                # click.echo(click.style(value, fg="green"))
                print(GREEN + value + DEFAULT, end='')
            elif key == "-":
                print(RED + value + DEFAULT, end='')
            else:
                print(value, end='')

            # print(self.changes)
