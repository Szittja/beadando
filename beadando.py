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

hotel = Szalloda("Szittja Hotel")

hotel.szoba_hozzaadas(EgyagyasSzoba("101", 50000))
hotel.szoba_hozzaadas(EgyagyasSzoba("102", 55000))
hotel.szoba_hozzaadas(KetagyasSzoba("103", 70000))

mainap = datetime.now().date()

for i in range(5):
    while True:
        random_szoba = random.choice(hotel.szobak)
        random_nap = mainap + timedelta(random.randint(0, 20))
        if hotel.foglal(random_szoba.szobaszam, random_nap):
            break

print(f"Üdvözöljük a {hotel.nev} foglalási rendszerében!")

while True:
    print("\nVálasszon az alábbi opciók közül:")
    print("1. Szobák listázása")
    print("2. Foglalások listázása")
    print("3. Szoba foglalás")
    print("4. Foglalás lemondása")
    print("0. Kilépés a foglaló rendszerből\n")
    valasztas = input("Kérem adja meg a kívánt opció számát: ")

    if valasztas == "1":
        hotel.szobak_listaja()

    elif valasztas == "2":
        hotel.foglalas_lista()

    elif valasztas == "3":
        while True:
            szobaszam = input("Adjon meg egy szobaszámot: ")
            szoba = next((sz for sz in hotel.szobak if sz.szobaszam == szobaszam), None)
            if szoba is None:
                print("Nincs ilyen szoba a szállodában.")
                hotel.szobak_listaja()
                continue
            while True:
                datum = input("Adja meg a dátumot (éééé-hh-nn formátumban): ")
                try:
                    datum = datetime.strptime(datum, "%Y-%m-%d").date()
                    if datum < mainap:
                        raise ValueError("Kérjük az aktuális vagy jövőbeli napot válasszon a foglalásra!")
                    break
                except ValueError as e:
                    print(str(e))
            foglal = hotel.foglal(szobaszam, datum)
            if foglal:
                print(f"A foglalás sikeres! Az ár: {foglal} Ft")
                break

    elif valasztas == "4":
        while True:
            szobaszam = input("Adjon meg egy szobaszámot: ")
            if not any(foglal.szoba.szobaszam == szobaszam for foglal in hotel.foglalasok):
                print("Nincs ilyen szobára foglalás a szállodában.")
                continue
            while True:
                datum = input("Adja meg a lemondandó foglalás dátumát (éééé-hh-nn formátumban): ")
                try:
                    datum = datetime.strptime(datum, "%Y-%m-%d").date()
                    if datum < mainap:
                        print("Csak jövőbeni foglalás mondható le.")
                    else:
                        break
                except ValueError:
                    print("Hibás dátum formátum!")
            if hotel.lemond(szobaszam, datum):
                print("A foglalás sikeresen lemondva.")
                break
            else:
                print("Nincs ilyen foglalás.")

    elif valasztas == "0":
        print("Köszönjük, hogy szállodánkat választotta. Viszont látásra!")
        break
    else:
        print("Hibás választás, kérjük próbálja újra.")