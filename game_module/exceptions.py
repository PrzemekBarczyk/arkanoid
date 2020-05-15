"""Moduł zawierający klasy wyjątków"""


class Exception(Exception):
    """Klasa główna wyjątku z której będą dziedziczyły wszystkie pozostałe"""
    def __init__(self, value):
        self.value = value
