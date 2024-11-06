ncrList = [21.42, 'hello', 3, 4, 'salam alaykom', False, 3.14150]

def ncrPARAMS(ism):
    print(f"Salam {ism}")

class Montaj:
    no3 = "HATIF"
    def __init__(self, id, ism, wasf, taman, majmo3):
        self.id = id
        self.ism = ism
        self.wasf = wasf
        self.taman = taman
        self.majmo3 = majmo3

    def takhfid(self, khasya, kima):
        if khasya == "taman" : 
            self.taman = self.taman - float(kima)
        else:
            self.majmo3 = self.majmo3 - int(kima)