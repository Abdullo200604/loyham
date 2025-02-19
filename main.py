from model import Shifokor, Bemor, TibbiyotMarkazi

# Interaktiv menyu
def menu():
    print("\n--- Abdulloh Tibbiyot Markazi Menyusi ---")
    print("1. Shifokor qo'shish")
    print("2. Bemor qo'shish")
    print("3. Qabul rejalashtirish")
    print("4. Ma'lumotlarni ko'rish")
    print("5. Ma'lumotlarni saqlash va chiqish")
    print("6. Shifokorni ro'yxatdan olib tashlash")
    print("7. Bemorni ro'yxatdan olib tashlash")
    tanlov = input("Tanlang (1/2/3/4/5/6/7): ")
    return tanlov

# Foydalanish
if __name__ == "__main__":
    markaz = TibbiyotMarkazi()
    markaz.malumot_yuklash()

    while True:
        tanlov = menu()

        if tanlov == "1":
            # Shifokor qo'shish
            ism = input("Shifokor ismi: ")
            yosh = int(input("Shifokor yoshi: "))
            mutaxassislik = input("Mutaxassisligi: ")
            shifokor = Shifokor(ism, yosh, mutaxassislik)
            markaz.shifokor_qoshish(shifokor)
            print(f"{ism} muvaffaqiyatli qo'shildi!")

        elif tanlov == "2":
            # Bemor qo'shish
            ism = input("Bemor ismi: ")
            yosh = int(input("Bemor yoshi: "))
            kasallik = input("Kasalligi: ")
            bemor = Bemor(ism, yosh, kasallik)
            markaz.bemor_qoshish(bemor)
            print(f"{ism} muvaffaqiyatli qo'shildi!")

        elif tanlov == "3":
            # Qabul rejalashtirish
            print("Mavjud shifokorlar:")
            for i, shifokor in enumerate(markaz.shifokorlar, 1):
                print(f"{i}. {shifokor.malumot_olish()}")
            shifokor_index = int(input("Shifokorni tanlang (raqam): ")) - 1

            print("Mavjud bemorlar:")
            for i, bemor in enumerate(markaz.bemorlar, 1):
                print(f"{i}. {bemor.malumot_olish()}")
            bemor_index = int(input("Bemorni tanlang (raqam): ")) - 1

            sana = input("Qabul sanasini kiriting (yyyy-mm-dd): ")
            markaz.qabul_rejalashtirish(markaz.shifokorlar[shifokor_index], markaz.bemorlar[bemor_index], sana)
            print("Qabul muvaffaqiyatli rejalashtirildi!")

        elif tanlov == "4":
            # Ma'lumotlarni ko'rish
            print("\n--- Shifokorlar ---")
            for shifokor in markaz.shifokorlar:
                print(shifokor.malumot_olish())

            print("\n--- Bemorlar ---")
            for bemor in markaz.bemorlar:
                print(bemor.malumot_olish())

            print("\n--- Qabullar ---")
            for qabul in markaz.qabullar:
                print(qabul.tafsilotlar())

            print("\n--- Ish vaqti ---")
            print(markaz.ish_vaqti.malumot_olish())

        elif tanlov == "5":
            # Ma'lumotlarni saqlash va chiqish
            markaz.malumot_saqlash()
            print("Ma'lumotlar saqlandi. Dasturdan chiqildi.")
            break

        elif tanlov == "6":
            # Shifokorni ro'yxatdan olib tashlash
            ism = input("Olib tashlanadigan shifokor ismi: ")
            markaz.shifokor_olib_tashlash(ism)

        elif tanlov == "7":
            # Bemorni ro'yxatdan olib tashlash
            ism = input("Olib tashlanadigan bemor ismi: ")
            markaz.bemor_olib_tashlash(ism)

        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")