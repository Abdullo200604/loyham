# Albatta! Kodni oddiy va tushunarli qilib tushuntiraman. Bizning dasturimiz
# **tibbiyot markazi** uchun ishlaydi va quyidagi asosiy vazifalarni bajaradi:
#
# 1. **Shifokor qo'shish**.
# 2. **Bemor qo'shish**.
# 3. **Qabul rejalashtirish** (shifokor va bemor o'rtasida).
# 4. **Ma'lumotlarni ko'rish** (shifokorlar, bemorlar, qabullar va ish vaqti).
# 5. **Shifokor yoki bemorni ro'yxatdan olib tashlash**.
# 6. **Ma'lumotlarni saqlash va yuklash** (JSON faylida).
#
# Kodni qismlarga bo'lib, har bir qismni oddiy tilda tushuntiramiz.
#
# ---
#
# ### 1. Asosiy Tushunchalar
#
# #### a) **Abstrakt Sinf (`Odam`)**
# - `Odam` sinfi barcha odamlar uchun umumiy xususiyatlarni belgilaydi:
#   - `_ism` (shaxsning ismi).
#   - `_yosh` (shaxsning yoshi).
# - Bu sinf **abstrakt**, ya'ni uni to'g'ridan-to'g'ri ishlatib bo'lmaydi.
# Buning o'rniga uning vorislari (`Shifokor` va `Bemor`) ishlatiladi.
# - `malumot_olish()` metodi har bir vorisda turlicha ishlaydi.
#
# ```python
# class Odam(ABC):
#     def __init__(self, ism, yosh):
#         self._ism = ism  # Inkapsulyatsiya
#         self._yosh = yosh
#
#     @abstractmethod
#     def malumot_olish(self):
#         pass
# ```
#
# ---
#
# #### b) **Shifokor va Bemor Sinflari**
# - `Shifokor` va `Bemor` sinflari `Odam` sinfidan meros oladi.
# - Har bir sinf o'ziga xos qo'shimcha ma'lumotlarga ega:
#   - Shifokorda `mutaxassislik` (masalan, "Nevrolog").
#   - Bemorda `kasallik` (masalan, "Gripp").
#
# ```python
# class Shifokor(Odam):
#     def __init__(self, ism, yosh, mutaxassislik):
#         super().__init__(ism, yosh)
#         self.mutaxassislik = mutaxassislik
#
#     def malumot_olish(self):
#         return f"Dr. {self._ism}, {self.mutaxassislik}, {self._yosh} yosh"
#
# class Bemor(Odam):
#     def __init__(self, ism, yosh, kasallik):
#         super().__init__(ism, yosh)
#         self.kasallik = kasallik
#
#     def malumot_olish(self):
#         return f"Bemor {self._ism}, {self.kasallik}, {self._yosh} yosh"
# ```
#
# ---
#
# ### 2. Qabul va Ish Vaqti
#
# #### a) **Qabul Sinfi**
# - `Qabul` sinfi shifokor va bemor o'rtasidagi qabulni ifodalaydi.
# - U quyidagi ma'lumotlarni saqlaydi:
#   - Qaysi shifokor bilan.
#   - Qaysi bemor bilan.
#   - Qabul sanasi.
#
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
#
# ---
#
# #### b) **Ish Vaqti Sinfi**
# - `IshVaqti` sinfi tibbiyot markazining ish vaqtini saqlaydi:
#   - Boshlanish va tugash vaqtlari.
#   - Tushlik va dam olish kunlari.
#
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
#         return f"Ish vaqti: {self.boshlanish}-{self.tugash},
#         Abet: {self.abet}, Shanba: {self.shanba}, Yakshanba: {self.yakshanba}"
# ```
#
# ---
#
# ### 3. Tibbiyot Markazi
#
# #### a) **TibbiyotMarkazi Sinfi**
# - Bu sinf butun tibbiyot markazini boshqaradi.
# - U quyidagi ro'yxatlarni saqlaydi:
#   - Shifokorlar.
#   - Bemorlar.
#   - Qabullar.
#   - Ish vaqti.
# - Ma'lumotlarni JSON faylida saqlash va yuklash imkoniyatiga ega.
#
# ```python
# class TibbiyotMarkazi:
#     def __init__(self):
#         self.shifokorlar = []
#         self.bemorlar = []
#         self.qabullar = []
#         self.ish_vaqti = IshVaqti("08:00", "18:00", "12:00-13:00", "08:00-12:00", "Dam olish")
#
#     def shifokor_qoshish(self, shifokor):
#         self.shifokorlar.append(shifokor)
#
#     def bemor_qoshish(self, bemor):
#         self.bemorlar.append(bemor)
#
#     def qabul_rejalashtirish(self, shifokor, bemor, sana):
#         qabul = Qabul(shifokor, bemor, sana)
#         self.qabullar.append(qabul)
#
#     def shifokor_olib_tashlash(self, ism):
#         for shifokor in self.shifokorlar:
#             if shifokor._ism == ism:
#                 self.shifokorlar.remove(shifokor)
#                 print(f"{ism} muvaffaqiyatli ro'yxatdan olib tashlandi!")
#                 return
#         print(f"{ism} topilmadi!")
#
#     def bemor_olib_tashlash(self, ism):
#         for bemor in self.bemorlar:
#             if bemor._ism == ism:
#                 self.bemorlar.remove(bemor)
#                 print(f"{ism} muvaffaqiyatli ro'yxatdan olib tashlandi!")
#                 return
#         print(f"{ism} topilmadi!")
#
#     def malumot_saqlash(self, fayl_nomi="jeyson.json"):
#         data = {
#             "shifokorlar": [{"ism": d._ism, "yosh": d._yosh, "mutaxassislik": d.mutaxassislik} for d in
#             self.shifokorlar],
#             "bemorlar": [{"ism": p._ism, "yosh": p._yosh, "kasallik": p.kasallik} for p in self.bemorlar],
#             "qabullar": [{"shifokor": a.shifokor._ism, "bemor": a.bemor._ism, "sana": a.sana} for a in self.qabullar],
#             "ish_vaqti": {
#                 "boshlanish": self.ish_vaqti.boshlanish,
#                 "tugash": self.ish_vaqti.tugash,
#                 "abet": self.ish_vaqti.abet,
#                 "shanba": self.ish_vaqti.shanba,
#                 "yakshanba": self.ish_vaqti.yakshanba
#             }
#         }
#         with open(fayl_nomi, "w") as fayl:
#             json.dump(data, fayl, indent=4)
#
#     def malumot_yuklash(self, fayl_nomi="jeyson.json"):
#         try:
#             with open(fayl_nomi, "r") as fayl:
#                 data = json.load(fayl)
#                 for d in data["shifokorlar"]:
#                     self.shifokorlar.append(Shifokor(d["ism"], d["yosh"], d["mutaxassislik"]))
#                 for p in data["bemorlar"]:
#                     self.bemorlar.append(Bemor(p["ism"], p["yosh"], p.get("kasallik", "Noma'lum")))
#                 self.ish_vaqti = IshVaqti(
#                     data["ish_vaqti"]["boshlanish"],
#                     data["ish_vaqti"]["tugash"],
#                     data["ish_vaqti"]["abet"],
#                     data["ish_vaqti"]["shanba"],
#                     data["ish_vaqti"]["yakshanba"]
#                 )
#         except FileNotFoundError:
#             print("Oldingi ma'lumotlar topilmadi.")
#         except json.JSONDecodeError:
#             print("Fayl ichidagi ma'lumotlar noto‘g‘ri formatda.")
# ```
#
# ---
#
# ### 4. Interaktiv Menyu
#
# Menyu orqali foydalanuvchi quyidagi amallarni bajara oladi:
# 1. **Shifokor qo'shish**.
# 2. **Bemor qo'shish**.
# 3. **Qabul rejalashtirish**.
# 4. **Ma'lumotlarni ko'rish**.
# 5. **Shifokorni ro'yxatdan olib tashlash**.
# 6. **Bemorni ro'yxatdan olib tashlash**.
# 7. **Dasturdan chiqish**.
#
# ```python
# def menu():
#     print("\n--- Tibbiyot Markazi Menyusi ---")
#     print("1. Shifokor qo'shish")
#     print("2. Bemor qo'shish")
#     print("3. Qabul rejalashtirish")
#     print("4. Ma'lumotlarni ko'rish")
#     print("5. Shifokorni ro'yxatdan olib tashlash")
#     print("6. Bemorni ro'yxatdan olib tashlash")
#     print("7. Ma'lumotlarni saqlash va chiqish")
#     tanlov = input("Tanlang (1/2/3/4/5/6/7): ")
#     return tanlov
# ```
#
# ---
#
# ### 5. Dasturni Ishga Tushirish
#
# ```python
# if __name__ == "__main__":
#     markaz = TibbiyotMarkazi()
#     markaz.malumot_yuklash()
#
#     while True:
#         tanlov = menu()
#
#         if tanlov == "1":
#             # Shifokor qo'shish
#             ism = input("Shifokor ismi: ")
#             yosh = int(input("Shifokor yoshi: "))
#             mutaxassislik = input("Mutaxassisligi: ")
#             shifokor = Shifokor(ism, yosh, mutaxassislik)
#             markaz.shifokor_qoshish(shifokor)
#             print(f"{ism} muvaffaqiyatli qo'shildi!")
#
#         elif tanlov == "2":
#             # Bemor qo'shish
#             ism = input("Bemor ismi: ")
#             yosh = int(input("Bemor yoshi: "))
#             kasallik = input("Kasalligi: ")
#             bemor = Bemor(ism, yosh, kasallik)
#             markaz.bemor_qoshish(bemor)
#             print(f"{ism} muvaffaqiyatli qo'shildi!")
#
#         elif tanlov == "3":
#             # Qabul rejalashtirish
#             print("Mavjud shifokorlar:")
#             for i, shifokor in enumerate(markaz.shifokorlar, 1):
#                 print(f"{i}. {shifokor.malumot_olish()}")
#             shifokor_index = int(input("Shifokorni tanlang (raqam): ")) - 1
#
#             print("Mavjud bemorlar:")
#             for i, bemor in enumerate(markaz.bemorlar, 1):
#                 print(f"{i}. {bemor.malumot_olish()}")
#             bemor_index = int(input("Bemorni tanlang (raqam): ")) - 1
#
#             sana = input("Qabul sanasini kiriting (yyyy-mm-dd): ")
#             markaz.qabul_rejalashtirish(markaz.shifokorlar[shifokor_index], markaz.bemorlar[bemor_index], sana)
#             print("Qabul muvaffaqiyatli rejalashtirildi!")
#
#         elif tanlov == "4":
#             # Ma'lumotlarni ko'rish
#             print("\n--- Shifokorlar ---")
#             for shifokor in markaz.shifokorlar:
#                 print(shifokor.malumot_olish())
#
#             print("\n--- Bemorlar ---")
#             for bemor in markaz.bemorlar:
#                 print(bemor.malumot_olish())
#
#             print("\n--- Qabullar ---")
#             for qabul in markaz.qabullar:
#                 print(qabul.tafsilotlar())
#
#             print("\n--- Ish vaqti ---")
#             print(markaz.ish_vaqti.malumot_olish())
#
#         elif tanlov == "5":
#             # Shifokorni ro'yxatdan olib tashlash
#             ism = input("Olib tashlanadigan shifokor ismi: ")
#             markaz.shifokor_olib_tashlash(ism)
#
#         elif tanlov == "6":
#             # Bemorni ro'yxatdan olib tashlash
#             ism = input("Olib tashlanadigan bemor ismi: ")
#             markaz.bemor_olib_tashlash(ism)
#
#         elif tanlov == "7":
#             # Ma'lumotlarni saqlash va chiqish
#             markaz.malumot_saqlash()
#             print("Ma'lumotlar saqlandi. Dasturdan chiqildi.")
#             break
#
#         else:
#             print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
# ```
#
# ---
#
# ### Natija:
#
# Dastur ishga tushganda menyu paydo bo'ladi. Foydalanuvchi menyu orqali shifokor qo'shishi, bemor qo'shishi,
# qabul rejalashtirishi, ma'lumotlarni ko'rishi, shifokor yoki bemorni ro'yxatdan olib tashlashi va ma'lumotlarni saqlashi mumkin.
#
# ---
#
# Bu kod endi oddiy va tushunarli! 😊a
