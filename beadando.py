from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import random

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def __str__(self):
        pass
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def __str__(self):
        return f"Egyágyas szoba {self.szobaszam}, Ár: {self.ar} Ft/éj"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def __str__(self):
        return f"Kétágyas szoba {self.szobaszam}, Ár: {self.ar} Ft/éj"
