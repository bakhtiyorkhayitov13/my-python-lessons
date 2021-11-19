
"""
Created on Thu Nov 18 21:25:01 2021

@author: Khayitov Bakhtiyor

Tema: Modullar
"""

def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka': karobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar 
    haqidagi ma'lumotlarni bittadan kiritish uchun funksiya"""
    avtolar = [] #salondagi avtolar uchun bo'sh ro'yhat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end=' ')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Karobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        #Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
        #lug'at shakllantirilib, har bir lug'atni ro'yhatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
        #Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni consolega chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} karobka, " 
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")








### bakhtiyor1308