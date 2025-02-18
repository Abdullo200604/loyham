import json


# 1. Abstrakt klass Shaxs
class Shaxs:
    def __init__(self, ism, yosh):
        self._ism = ism  # Encapsulation: Private property
        self._yosh = yosh

    def get_ism(self):
        return self._ism

    def get_yosh(self):
        return self._yosh

    def malumotlarni_korsat(self):
        raise NotImplementedError("Bu metod voris klasslar tomonidan qayta yozilishi kerak")


# 2. Doktor klassi
class Doktor(Shaxs):
    def __init__(self, ism, yosh, mutaxassislik):
        super().__init__(ism, yosh)
        self._mutaxassislik = mutaxassislik

    def malumotlarni_korsat(self):
        return f"Doktor: {self.get_ism()}, Mutaxassisligi: {self._mutaxassislik}"


# 3. Bemor klassi
class Bemor(Shaxs):
    def __init__(self, ism, yosh):
        super().__init__(ism, yosh)
        self._tibbiy_tarix = []

    def tibbiy_tarix_qoshish(self, kasallik, sana):
        self._tibbiy_tarix.append({"kasallik": kasallik, "sana": sana})

    def malumotlarni_korsat(self):
        tarix = "\n".join([f"Kasallik: {r['kasallik']}, Sana: {r['sana']}" for r in self._tibbiy_tarix])
        return f"Bemor: {self.get_ism()}, Yosh: {self.get_yosh()}\nTibbiy tarix:\n{tarix}"


# 4. Tibbiy Markaz klassi
class TibbiyMarkaz:
    def __init__(self):
        self.doktorlar = []
        self.bemorlar = []

    def doktor_qoshish(self, doktor):
        self.doktorlar.append(doktor)

    def bemor_qoshish(self, bemor):
        self.bemorlar.append(bemor)

    def barcha_malumotlarni_korsat(self):
        print("Doktorlar:")
        for doktor in self.doktorlar:
            print(doktor.malumotlarni_korsat())
        print("\nBemorlar:")
        for bemor in self.bemorlar:
            print(bemor.malumotlarni_korsat())


# 5. FaylBoshqaruvchi klassi
class FaylBoshqaruvchi:
    @staticmethod
    def saqlash_json(malumotlar, fayl_nomi="jeyson.json"):  # Fayl nomi o'zgartirildi
        with open(fayl_nomi, "w") as fayl:
            json.dump(malumotlar, fayl, indent=4)

    @staticmethod
    def yuklash_json(fayl_nomi="jeyson.json"):  # Fayl nomi o'zgartirildi
        try:
            with open(fayl_nomi, "r") as fayl:
                return json.load(fayl)
        except FileNotFoundError:
            return {"doktorlar": [], "bemorlar": []}


# Konsol ilovasi
def asosiy_dastur():
    markaz = TibbiyMarkaz()
    malumotlar = FaylBoshqaruvchi.yuklash_json()

    # Doktorlarni yuklash
    for doktor_data in malumotlar["doktorlar"]:
        doktor = Doktor(doktor_data["ism"], 30, doktor_data["mutaxassislik"])
        markaz.doktor_qoshish(doktor)

    # Bemorlarni yuklash
    for bemor_data in malumotlar["bemorlar"]:
        bemor = Bemor(bemor_data["ism"], bemor_data["yosh"])
        for tarix in bemor_data.get("tibbiy_tarix", []):
            bemor.tibbiy_tarix_qoshish(tarix["kasallik"], tarix["sana"])
        markaz.bemor_qoshish(bemor)

    while True:
        print("\n1. Doktor qo'shish")
        print("2. Bemor qo'shish")
        print("3. Barcha ma'lumotlarni ko'rish")
        print("4. Saqlash va chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            ism = input("Doktor ismini kiriting: ")
            mutaxassislik = input("Doktor mutaxassisligini kiriting: ")
            doktor = Doktor(ism, 30, mutaxassislik)
            markaz.doktor_qoshish(doktor)
        elif tanlov == "2":
            ism = input("Bemor ismini kiriting: ")
            yosh = int(input("Bemor yoshini kiriting: "))
            bemor = Bemor(ism, yosh)
            markaz.bemor_qoshish(bemor)
        elif tanlov == "3":
            markaz.barcha_malumotlarni_korsat()
        elif tanlov == "4":
            # Ma'lumotlarni saqlash
            doktorlar_malumotlari = [{"ism": dok.get_ism(), "mutaxassislik": dok._mutaxassislik} for dok in
                                     markaz.doktorlar]
            bemorlar_malumotlari = [
                {
                    "ism": bem.get_ism(),
                    "yosh": bem.get_yosh(),
                    "tibbiy_tarix": bem._tibbiy_tarix
                } for bem in markaz.bemorlar
            ]
            FaylBoshqaruvchi.saqlash_json({"doktorlar": doktorlar_malumotlari, "bemorlar": bemorlar_malumotlari})
            print("Ma'lumotlar 'jeyson.json' fayliga saqlandi. Dasturdan chiqilmoqda...")
            break


if __name__ == "__main__":
    asosiy_dastur()
