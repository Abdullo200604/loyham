
# Tibbiyot Markazi Dasturi

Bu dastur tibbiyot markazini boshqarish uchun yaratilgan. U quyidagi vazifalarni bajaradi:

- Shifokorlarni ro'yxatga olish.
- Bemorlarni ro'yxatga olish.
- Qabul rejalashtirish (shifokor va bemor o'rtasida).
- Ma'lumotlarni ko'rish (shifokorlar, bemorlar, qabullar va ish vaqti).
- Shifokor yoki bemorni ro'yxatdan olib tashlash.
- Ma'lumotlarni JSON formatida saqlash va yuklash.

---

## Fayllar Tuzilishi

Loyihada ikkita asosiy fayl mavjud:

1. **`model.py`**:  
   - Bu yerda barcha sinflar (`Odam`, `Shifokor`, `Bemor`, `Qabul`, `IshVaqti`, `TibbiyotMarkazi`) joylashgan.
   - Sinflar va ularning metodlari bu faylda aniqlangan.

2. **`main.py`**:  
   - Bu faylda interaktiv menyu va foydalanuvchi bilan o'zaro aloqa amalga oshiriladi.
   - Foydalanuvchi menyu orqali shifokor qo'shishi, bemor qo'shishi, qabul rejalashtirishi va boshqa amallarni bajara oladi.

---

## O'rnatish Ko'rsatmalari

### 1. Python-ni O'rnatish
Dasturni ishga tushirish uchun sizda Python o'rnatilgan bo'lishi kerak. Python-ni quyidagi havoladan yuklab olish mumkin:  
[Python Rasmiy Sayt](https://www.python.org/downloads/)

### 2. Repository-ni Klonlash
GitHub repository-ni klonlash uchun quyidagi buyruqni terminalga yozing:

```bash
git clone https://github.com/sizning-reponing-url.git
```

### 3. Kerakli Kutubxonalarni O'rnatish
Ushbu loyihada maxsus kutubxonalar talab qilinmaydi, lekin agar sizda `json` yoki boshqa standart kutubxonalar yo'q bo'lsa, ular avtomatik ravishda Python bilan o'rnatiladi.

---

## Ishga Tushirish

### 1. Terminalni Ochish
Terminalni oching va loyihaning joylashgan papkasiga o'ting:

```bash
cd path/to/your/project/folder
```

### 2. Dasturni Ishga Tushirish
Quyidagi buyruqni yozing:

```bash
python main.py
```

Dastur ishga tushganda interaktiv menyu paydo bo'ladi. Menyu orqali quyidagi amallarni bajara olasiz:

- **Shifokor qo'shish**.
- **Bemor qo'shish**.
- **Qabul rejalashtirish**.
- **Ma'lumotlarni ko'rish**.
- **Shifokorni ro'yxatdan olib tashlash**.
- **Bemorni ro'yxatdan olib tashlash**.
- **Ma'lumotlarni saqlash va chiqish**.

---

## Misol

#### 1. Shifokor Qo'shish
```plaintext
--- Tibbiyot Markazi Menyusi ---
1. Shifokor qo'shish
2. Bemor qo'shish
3. Qabul rejalashtirish
4. Ma'lumotlarni ko'rish
5. Shifokorni ro'yxatdan olib tashlash
6. Bemorni ro'yxatdan olib tashlash
7. Ma'lumotlarni saqlash va chiqish
Tanlang (1/2/3/4/5/6/7): 1
Shifokor ismi: Abdulloh
Shifokor yoshi: 40
Mutaxassisligi: Nevrolog
Abdulloh muvaffaqiyatli qo'shildi!
```

#### 2. Ma'lumotlarni Ko'rish
```plaintext
--- Tibbiyot Markazi Menyusi ---
1. Shifokor qo'shish
2. Bemor qo'shish
3. Qabul rejalashtirish
4. Ma'lumotlarni ko'rish
5. Shifokorni ro'yxatdan olib tashlash
6. Bemorni ro'yxatdan olib tashlash
7. Ma'lumotlarni saqlash va chiqish
Tanlang (1/2/3/4/5/6/7): 4

--- Shifokorlar ---
Dr. Abdulloh, Nevrolog, 40 yosh

--- Bemorlar ---

--- Qabullar ---

--- Ish vaqti ---
Ish vaqti: 08:00-18:00, Abet: 12:00-13:00, Shanba: 08:00-12:00, Yakshanba: Dam olish
```

---

## Fayllar

### 1. `model.py`
Bu faylda barcha sinflar va ularning metodlari joylashgan. Sinflar quyidagilarni ifodalaydi:
- **`Odam`**: Asosiy abstrakt sinf.
- **`Shifokor`**: Shifokorlarni tasvirlaydi.
- **`Bemor`**: Bemorlarni tasvirlaydi.
- **`Qabul`**: Qabul jarayonini tasvirlaydi.
- **`IshVaqti`**: Ish vaqtini tasvirlaydi.
- **`TibbiyotMarkazi`**: Tibbiyot markazining barcha funksiyalarini boshqaradi.

### 2. `main.py`
Bu faylda interaktiv menyu va foydalanuvchi bilan o'zaro aloqa amalga oshiriladi.

---

## Ma'lumotlar Saqlash

Ma'lumotlar JSON formatida saqlanadi va `jeyson.json` nomli faylda saqlanadi. Agar siz dasturni ishlatib bo'lgandan keyin uni qayta ishga tushirsangiz, oldingi ma'lumotlar avtomatik ravishda yuklanadi.

---

## Aloqaga Chiqish

Agar sizda savollar yoki takliflar bo'lsa, quyidagi manzillar orqali men bilan bog'lanishingiz mumkin:

- **GitHub**: https://github.com/Abdullo200604
- **Email**: lwcardina12@gmail.com

---

Bu README fayli sizning loyihangizni tushunarli va professional tarzda taqdim etadi. 🚀
