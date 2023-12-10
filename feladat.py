from abc import ABC, abstractmethod
import datetime

class Bicikli(ABC):
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot

class OrszagutiBicikli(Bicikli):
    def __init__(self, ar, allapot):
        super().__init__("OrszagutiBicikli", ar, allapot)

class HegyiBicikli(Bicikli):
    def __init__(self, ar, allapot):
        super().__init__("HegyiBicikli", ar, allapot)


class Kolcsonzo():
    def __init__(self, nev, biciklik):
        self.nev = nev
        self.biciklik = biciklik
        self.kolcsonzesek = []

    def listaz_kolcsonzes(self):
        if not self.kolcsonzesek:
            print("Nincsenek kölcsönzések")
            return

        for kolcsonzes in self.kolcsonzesek:
            bicikli = kolcsonzes.bicikli
            print("Kölcsönzés adatai:\n név: {}\n mettől: {}\n meddig: {}\n ára: {}\n bicikli típusa: {} állapota: {}\n".format(kolcsonzes.nev, kolcsonzes.mettol.strftime("%Y-%m-%d"), kolcsonzes.meddig.strftime("%Y-%m-%d"), kolcsonzes.ar(), bicikli.tipus, bicikli.allapot))

    def listaz_biciklik(self):
        for i in range(len(self.biciklik)):
            bicikli = self.biciklik[i]
            print("{}: \n típus: {}\n ár: {}\n állapot: {}\n".format(i+1, bicikli.tipus, bicikli.ar, bicikli.allapot))

    def hozzaad_kolcsonzes(self, ujkolcsonzes):
        for kolcsonzes in self.kolcsonzesek:
            if kolcsonzes.bicikli == ujkolcsonzes.bicikli: 
                if kolcsonzes.mettol <= ujkolcsonzes.mettol <= kolcsonzes.meddig or kolcsonzes.mettol <= ujkolcsonzes.meddig <= kolcsonzes.meddig:
                    print("Ez a bicikli már ki van kölcsönözve erre a dátumra!")
                    return
            if datetime.date.today() > ujkolcsonzes.mettol.date():
                print("A megadott dátum nem jövőbeli!")
                return

        self.kolcsonzesek.append(ujkolcsonzes)
    
    def torol_kolcsonzes(self, nev):
        for kolcsonzes in self.kolcsonzesek:
            if kolcsonzes.nev == nev:
                if datetime.date.today() > kolcsonzes.mettol.date():
                    print("Csak jövőbeni foglalások törölhetőek!")
                    return

                self.kolcsonzesek.remove(kolcsonzes)
                break



class Kolcsonzes():
    def __init__(self, nev, bicikli, mettol, meddig):
        self.nev = nev
        self.bicikli = bicikli
        self.mettol = mettol
        self.meddig = meddig

    def ar(self):
        return (self.meddig-self.mettol).days * self.bicikli.ar


hegyibicikli1 = HegyiBicikli(10000, "viseletes")
hegyibicikli2 = HegyiBicikli(12000, "új")
orszagutibicikli1 = OrszagutiBicikli(6000, "új")
kolcsonzo = Kolcsonzo("Bicikli kölcsönző", [hegyibicikli1, hegyibicikli2, orszagutibicikli1])

kolcsonzo.hozzaad_kolcsonzes(Kolcsonzes("nev1", hegyibicikli1, datetime.datetime(2023, 12, 10), datetime.datetime(2023, 12, 12)))

def print_menu():  
    print("1: kölcsönzés")
    print("2: lemondás")
    print("3: listázás")
    print("9: kilépés")

def datum():
    ev = int(input("Év: ")) 
    honap = int(input("Hónap: "))
    nap = int(input("Nap: "))  
    return datetime.datetime(ev, honap, nap)

inp = 0

while inp != 9:
    print_menu()
    inp = int(input("menü: "))
    if inp == 1:
        kolcsonzo.listaz_biciklik()
        bicikli = int(input("Választott bicikli: "))-1
        nev = str(input("Adja meg a nevét: "))
        print("Mettől: ")
        mettol = datum()
        print("Meddig: ")
        meddig = datum()
        kolcsonzo.hozzaad_kolcsonzes(Kolcsonzes(nev, kolcsonzo.biciklik[bicikli], mettol, meddig))

    if inp == 2:
        nev = str(input("Adja meg a nevét: "))
        kolcsonzo.torol_kolcsonzes(nev)

    if inp == 3:
        kolcsonzo.listaz_kolcsonzes()