#!/usr/bin/python3
"""MyInt class Module"""


class MyInt(int):
    """Custom Int Class"""

    def __eq__(self, __value: object) -> bool:
        return int(self) != __value

    def __ne__(self, __value: object) -> bool:
        return int(self) == __value
