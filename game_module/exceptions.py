"""Moduł zawierający klasy wyjątków"""


class Exception(Exception):
    def __init__(self, value):
        self.value = value
