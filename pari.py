class Odam:
    def __init__(self, ism, fam, yosh):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh

    def shifri(self):
        print(self.ism, self.fam, self.yosh)
    
class Oshpaz(Odam):
    def __init__(self, ism, fam, yosh, taom):
        super().__init__(ism, fam, yosh)
        self.taom = taom

    def shifri(self):
        print(self.ism, self.fam, self.yosh, self.taom)

class Sutdent(Odam):
    def __init__(self, ism, fam, yosh,  kasibi):
        super().__init__(ism, fam, yosh)
        self.kasibi = kasibi

    def shifri(self):
        print(self.ism, self.fam, self.yosh, self.kasibi)

class Ishi(Odam):
    def __init__(self, ism, fam, yosh, qanaqa):
        super().__init__(ism, fam, yosh)
        self.qanaqa = qanaqa

    def shifri(self):
        print(self.ism, self.fam, self.yosh, self.qanaqa)
        
a = Odam("Fariza", "Turekhanova", "18")
a2 = Oshpaz("Pakizat", "Kulbarakova", "19", "osh")
a3 = Sutdent("Albina", "Suleymenova", "17", "pedagogika")
a4 = Ishi("Esen", "Batirxanov", "18", "satrudnik")

a.shifri()
a2.shifri()
a3.shifri()
a4.shifri() 

