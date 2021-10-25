# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

### Lug'at
talaba_01 = {'ism':'baxtiyor xayitov', 'yosh':30, 't_yili':1991}
print(talaba_01['ism'].title())

## Lug'atda istalgan ma'lumot turlarini qo'shish mumkin
print(f"{talaba_01['ism'].title()},\
 {talaba_01['t_yili']}-yilda tug'ilgan,\
 {talaba_01['yosh']} yoshda")

## Lug'atga yangi kalit so'z va qiymt qo'shish
talaba_01['kurs'] = 4
talaba_01['fakultet'] = 'iqtisodiyot'
talaba_01['hobbiy'] = "til o'rganish"
print(talaba_01)

## Bo'sh lug'at
talaba_02 = {}
talaba_02['ism'] = 'imom rahmonov'
talaba_02['kurs'] = 3
talaba_02['yosh'] = 19
print(talaba_02)
print(f"Talaba {talaba_02['ism'].title()} {talaba_02['kurs']}-kursda o'qiydi.")

## Qiymatlarni yangilash
talaba_02['kurs'] = 4
print(f"Talaba {talaba_02['ism'].title()} {talaba_02['kurs']}-kursga o'tdi.")

## Kalit so'z yoki qiymatni o'chirib tashlash
talaba_03 = {'ism':'baxtiyor xayitov', 'yosh':30, 't_yili':1991}
print(talaba_03)
del talaba_03['yosh']
print(talaba_03)

## Lug'atlarni bir necha qatorlarda yozish
telefonlar = {
    'ali':'ipohe x',
    'vali':'galaxy 9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'sobir':'fly 10'
    }
print(telefonlar['vali'])

## .get() metodi
phone = telefonlar.get('hasan', 'Bunday ism mavjud emas!')
print(phone)

## None javobi chiqadigan variant
phone = telefonlar.get('hasan')
print(phone)

### Lug'at bilan ishlaymiz
# .item() metodi bilan ishlash
print(telefonlar.items())
for key, value in telefonlar.items():
    print(f"Key: {key}")
    print(f"Valey: {value}")
for k, v in telefonlar.items():
    print(f"{k.title()}ning telefoni {v}.")

# .keys() metodi bilan ishlash
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
#print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar:
    print(mahsulot.title())
#tepadagi 2 ta variantdaham kalit so'zlar consolga chiqadi

bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling.")

## Lug'at elementlarini tartib bilan chiqarish o'rganamiz

# .sorted() funksiyasidan foydalanish
print('Do\'kondagi mahsulotlar:')
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# .values() metodidan foydalanish
print(telefonlar.values())

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)

# .set() funksiyasidan foydalanish
mobil_telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy 9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'sobir':'fly 10',
    'temur':'iphone x',
    'ikrom':'galaxy 9',
    'islom':'iphone x'
    }
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for mobile in set(mobil_telefonlar.values()):
    print(mobile)

toys = {"ball", "car", "lamp", "ball", "rocket", 'car'}
print(type(toys))
print(toys)

### bakhtiyor1308