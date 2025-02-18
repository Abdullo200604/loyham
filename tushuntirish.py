# Bu kod **Tibbiyot Markazi** uchun **obyektga yo‘naltirilgan dasturlash (OOP)** prinsiplari asosida yozilgan **konsol ilova**. Unda **inheritance (meros olish), polymorphism (ko‘p qiyofalik), encapsulation (inkapsulyatsiya), abstraction (abstraksiya)** qo‘llanilgan. Kod **shifokorlar, bemorlar, qabullar** va **ish vaqti** bilan ishlaydi. Ma'lumotlar **jeyson.json** faylga saqlanadi.
#
# ---
#
# ## **1. Kutubxonalarni import qilish**
# ```python
# import json
# from abc import ABC, abstractmethod
# ```
# - `json` – Ma'lumotlarni JSON faylga saqlash va yuklash uchun ishlatiladi.
# - `ABC` va `abstractmethod` – Abstrakt klass yaratish uchun ishlatiladi.
#
# ---
#
# ## **2. Abstrakt sinf (`Odam`)**
# ```python
# class Odam(ABC):
#     def __init__(self, ism, yosh):
#         self._ism = ism  # Inkapsulyatsiya (xususiy o‘zgaruvchi)
#         self._yosh = yosh
#
#     @abstractmethod
#     def malumot_olish(self):
#         pass
# ```
# - **Abstrakt sinf** – `Odam` boshqa klasslar uchun **asos** bo‘ladi.
# - **Inkapsulyatsiya** – `_ism` va `_yosh` o‘zgaruvchilari `protected`, ya'ni tashqaridan to‘g‘ridan-to‘g‘ri chaqirib bo‘lmaydi.
# - `malumot_olish` metodi **abstrakt** – uni `Odam`ni meros olgan klasslar bajarishi kerak.
#
# ---
#
# ## **3. Shifokor va Bemor klasslari (`Odam`dan meros olgan)**
# ```python
# class Shifokor(Odam):
#     def __init__(self, ism, yosh, mutaxassislik):
#         super().__init__(ism, yosh)
#         self.mutaxassislik = mutaxassislik
#
#     def malumot_olish(self):
#         return f"Dr. {self._ism}, {self.mutaxassislik}, {self._yosh} yosh"
# ```
# - `Shifokor` **Odam** klassidan meros oladi.
# - `super().__init__(ism, yosh)` – **ota klassning (`Odam`) konstruktorini** chaqirish.
# - `malumot_olish` metodi **o‘ziga xos ko‘rinishda ishlaydi** (polimorfizm).
#
# ---
# ```python
# class Bemor(Odam):
#     def __init__(self, ism, yosh, kasallik):
#         super().__init__(ism, yosh)
#         self.kasallik = kasallik
#
#     def malumot_olish(self):
#         return f"Bemor {self._ism}, {self.kasallik}, {self._yosh} yosh"
# ```
# - **Huddi shifokor kabi**, lekin bu yerda `kasallik` atributi bor.
#
# ---
#
# ## **4. Qabul klassi**
# ```python
# class Qabul:
#     def __init__(self, shifokor, bemor, sana):
#         self.shifokor = shifokor
#         self.bemor = bemor
#         self.sana = sana
#
#     def tafsilotlar(self):
#         return f"Qabul: {self.bemor._ism} {self.shifokor._ism} bilan {self.sana} kuni"
# ```
# - **Qabul** – shifokor va bemor uchrashuvi.
# - `tafsilotlar()` metodi – **qabul haqida ma’lumot** qaytaradi.
#
# ---
#
# ## **5. Ish vaqti klassi**
# ```python
# class IshVaqti:
#     def __init__(self, boshlanish, tugash, abet, shanba, yakshanba):
#         self.boshlanish = boshlanish
#         self.tugash = tugash
#         self.abet = abet
#         self.shanba = shanba
#         self.yakshanba = yakshanba
#
#     def malumot_olish(self):
#         return f"Ish vaqti: {self.boshlanish}-{self.tugash}, Abet: {self.abet}, Shanba: {self.shanba}, Yakshanba: {self.yakshanba}"
# ```
# - **Ish vaqtlarini belgilaydi**.
# - `malumot_olish()` metodi – ish vaqti haqida **matn** qaytaradi.
#
# ---
#
# ## **6. Tibbiyot markazi klassi**
# ```python
# class TibbiyotMarkazi:
#     def __init__(self):
#         self.shifokorlar = []
#         self.bemorlar = []
#         self.qabullar = []
#         self.ish_vaqti = IshVaqti("08:00", "18:00", "12:00-13:00", "08:00-12:00", "Dam olish")
# ```
# - **Tibbiyot markazida** shifokorlar, bemorlar, qabullar va **ish vaqti** mavjud.
#
# ---
#
# ### **Shifokor va bemor qo‘shish funksiyalari**
# ```python
# def shifokor_qoshish(self, shifokor):
#     self.shifokorlar.append(shifokor)
#
# def bemor_qoshish(self, bemor):
#     self.bemorlar.append(bemor)
# ```
# - **Shifokor va bemorlarni ro‘yxatga qo‘shadi**.
#
# ---
#
# ### **Qabul rejalashtirish**
# ```python
# def qabul_rejalashtirish(self, shifokor, bemor, sana):
#     qabul = Qabul(shifokor, bemor, sana)
#     self.qabullar.append(qabul)
# ```
# - **Shifokor va bemor uchun qabulni rejalashtiradi**.
#
# ---
#
# ### **JSON ma'lumotlarni saqlash**
# ```python
# def malumot_saqlash(self, fayl_nomi="jeyson.json"):
#     data = {
#         "shifokorlar": [{"ism": d._ism, "yosh": d._yosh, "mutaxassislik": d.mutaxassislik} for d in self.shifokorlar],
#         "bemorlar": [{"ism": p._ism, "yosh": p._yosh, "kasallik": p.kasallik} for p in self.bemorlar],
#         "qabullar": [{"shifokor": a.shifokor._ism, "bemor": a.bemor._ism, "sana": a.sana} for a in self.qabullar],
#         "ish_vaqti": {"boshlanish": self.ish_vaqti.boshlanish, "tugash": self.ish_vaqti.tugash, "abet": self.ish_vaqti.abet, "shanba": self.ish_vaqti.shanba, "yakshanba": self.ish_vaqti.yakshanba}
#     }
#     with open(fayl_nomi, "w") as fayl:
#         json.dump(data, fayl, indent=4)
# ```
# - **Ma'lumotlarni JSON faylga yozadi**.
#
# ---
#
# ### **JSON ma'lumotlarni yuklash**
# ```python
# def malumot_yuklash(self, fayl_nomi="jeyson.json"):
#     try:
#         with open(fayl_nomi, "r") as fayl:
#             data = json.load(fayl)
#             for d in data["shifokorlar"]:
#                 self.shifokorlar.append(Shifokor(d["ism"], d["yosh"], d["mutaxassislik"]))
#             for p in data["bemorlar"]:
#                 self.bemorlar.append(Bemor(p["ism"], p["yosh"], p["kasallik"]))
#             self.ish_vaqti = IshVaqti(data["ish_vaqti"]["boshlanish"], data["ish_vaqti"]["tugash"], data["ish_vaqti"]["abet"], data["ish_vaqti"]["shanba"], data["ish_vaqti"]["yakshanba"])
#     except FileNotFoundError:
#         print("Oldingi ma'lumotlar topilmadi.")
# ```
# - **Fayldan ma'lumotlarni yuklab oladi**.
#
# ---
#
# ### **Dastur ishga tushishi**
# ```python
# markaz = TibbiyotMarkazi()
# markaz.malumot_yuklash()
#
# s1 = Shifokor("Ali Karimov", 50, "Nevrolog")
# b1 = Bemor("Shahnoza", 28, "Gripp")
#
# markaz.shifokor_qoshish(s1)
# markaz.bemor_qoshish(b1)
# markaz.qabul_rejalashtirish(s1, b1, "2025-02-18")
#
# markaz.malumot_saqlash()
# print(markaz.ish_vaqti.malumot_olish())
# ```
# - **Ma'lumotlarni saqlaydi va chiqaradi**.