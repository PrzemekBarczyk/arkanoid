"""Moduł zawierający klasy wyjątków"""


class MyException(Exception):
    """Klasa główna wyjątku z której będą dziedziczyły wszystkie pozostałe"""

    def __init__(self, value):
        super().__init__()
        self.value = value
