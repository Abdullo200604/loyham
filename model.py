import json
from abc import ABC, abstractmethod

# Abstrakt sinf (Odam)
class Odam(ABC):
    def __init__(self, ism, yosh):
        self._ism = ism  # Inkapsulyatsiya
        self._yosh = yosh

    @abstractmethod
    def malumot_olish(self):
        pass

# Shifokor sinfi (Odamdan meros olgan)
class Shifokor(Odam):
    def __init__(self, ism, yosh, mutaxassislik):
        super().__init__(ism, yosh)
        self.mutaxassislik = mutaxassislik

    def malumot_olish(self):
        return f"Dr. {self._ism}, {self.mutaxassislik}, {self._yosh} yosh"

# Bemor sinfi (Odamdan meros olgan)
class Bemor(Odam):
    def __init__(self, ism, yosh, kasallik):
        super().__init__(ism, yosh)
        self.kasallik = kasallik

    def malumot_olish(self):
        return f"Bemor {self._ism}, {self.kasallik}, {self._yosh} yosh"

# Qabul sinfi
class Qabul:
    def __init__(self, shifokor, bemor, sana):
        self.shifokor = shifokor
        self.bemor = bemor
        self.sana = sana

    def tafsilotlar(self):
        return f"Qabul: {self.bemor._ism} {self.shifokor._ism} bilan {self.sana} kuni"

# Ish vaqti sinfi
class IshVaqti:
    def __init__(self, boshlanish, tugash, abet, shanba, yakshanba):
        self.boshlanish = boshlanish
        self.tugash = tugash
        self.abet = abet
        self.shanba = shanba
        self.yakshanba = yakshanba

    def malumot_olish(self):
        return f"Ish vaqti: {self.boshlanish}-{self.tugash}, Abet: {self.abet}, Shanba: {self.shanba}, Yakshanba: {self.yakshanba}"

# Tibbiyot markazi sinfi
class TibbiyotMarkazi:
    def __init__(self):
        self.shifokorlar = []
        self.bemorlar = []
        self.qabullar = []
        self.ish_vaqti = IshVaqti("08:00", "18:00", "12:00-13:00", "08:00-12:00", "Dam olish")

    def shifokor_qoshish(self, shifokor):
        self.shifokorlar.append(shifokor)

    def bemor_qoshish(self, bemor):
        self.bemorlar.append(bemor)

    def qabul_rejalashtirish(self, shifokor, bemor, sana):
        qabul = Qabul(shifokor, bemor, sana)
        self.qabullar.append(qabul)

    def shifokor_olib_tashlash(self, ism):
        for shifokor in self.shifokorlar:
            if shifokor._ism == ism:
                self.shifokorlar.remove(shifokor)
                print(f"{ism} muvaffaqiyatli ro'yxatdan olib tashlandi!")
                return
        print(f"{ism} topilmadi!")

    def bemor_olib_tashlash(self, ism):
        for bemor in self.bemorlar:
            if bemor._ism == ism:
                self.bemorlar.remove(bemor)
                print(f"{ism} muvaffaqiyatli ro'yxatdan olib tashlandi!")
                return
        print(f"{ism} topilmadi!")

    def malumot_saqlash(self, fayl_nomi="jeyson.json"):
        data = {
            "shifokorlar": [{"ism": d._ism, "yosh": d._yosh, "mutaxassislik": d.mutaxassislik} for d in self.shifokorlar],
            "bemorlar": [{"ism": p._ism, "yosh": p._yosh, "kasallik": p.kasallik} for p in self.bemorlar],
            "qabullar": [{"shifokor": a.shifokor._ism, "bemor": a.bemor._ism, "sana": a.sana} for a in self.qabullar],
            "ish_vaqti": {
                "boshlanish": self.ish_vaqti.boshlanish,
                "tugash": self.ish_vaqti.tugash,
                "abet": self.ish_vaqti.abet,
                "shanba": self.ish_vaqti.shanba,
                "yakshanba": self.ish_vaqti.yakshanba
            }
        }
        with open(fayl_nomi, "w") as fayl:
            json.dump(data, fayl, indent=4)

    def malumot_yuklash(self, fayl_nomi="jeyson.json"):
        try:
            with open(fayl_nomi, "r") as fayl:
                data = json.load(fayl)
                for d in data["shifokorlar"]:
                    self.shifokorlar.append(Shifokor(d["ism"], d["yosh"], d["mutaxassislik"]))
                for p in data["bemorlar"]:
                    self.bemorlar.append(Bemor(p["ism"], p["yosh"], p.get("kasallik", "Noma'lum")))
                self.ish_vaqti = IshVaqti(
                    data["ish_vaqti"]["boshlanish"],
                    data["ish_vaqti"]["tugash"],
                    data["ish_vaqti"]["abet"],
                    data["ish_vaqti"]["shanba"],
                    data["ish_vaqti"]["yakshanba"]
                )
        except FileNotFoundError:
            print("Oldingi ma'lumotlar topilmadi.")
        except json.JSONDecodeError:
            print("Fayl ichidagi ma'lumotlar noto‘g‘ri formatda.")