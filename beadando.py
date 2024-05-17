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


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for foglal in self.foglalasok:
            if foglal.szoba.szobaszam == szobaszam and foglal.datum == datum:
                print("A szoba már foglalt ezen a napon, válasszon másik szobát vagy dátumot!")
                return None
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        return None

    def lemond(self, szobaszam, datum):
        for foglal in self.foglalasok:
            if foglal.szoba.szobaszam == szobaszam and foglal.datum == datum:
                self.foglalasok.remove(foglal)
                return True
        return False

    def foglalas_lista(self):
        print("Foglalások listája:")
        for foglal in self.foglalasok:
            print(f"Szoba: {foglal.szoba.szobaszam}, Dátum: {foglal.datum}")

    def szobak_listaja(self):
        print("Szobák listája:")
        for szoba in self.szobak:
            print(szoba)
