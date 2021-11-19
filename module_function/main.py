
"""
Created on Thu Nov 18 21:25:01 2021

@author: Khayitov Bakhtiyor

Tema: Modullar
"""

# import avto_info_module

# avto1 = avto_info_module.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# avto_info_module.info_print(avto1)

#modul nomini qisqartirish usuli pastda

# import avto_info_module as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# aim.info_print(avto1)

#moduldan funksiyalarni chaqirib olishning yana bir boshqa usuli pastda

# from avto_info_module import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

#moduldan chaqirayotgan funksiyalar nomini qisqartirish usuli pastda

# from avto_info_module import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# iprint(avto1)

#moduldan funksiyalarni chaqirib olishning yana bir boshqa qisqaroq usuli pastda

# from avto_info_module import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

#ammo bu usul tavsiya qilinmaydi, sababi pythonni o'zidagi va o'zimiz yaratgan 
#katta modullar ichida ko'plab funksiyalar va o'zgaruvchilar bo'ladi,
#dastur yozish davomida ularning nomi bir xil bo'lib qolishi va dasturda xatolik yuzaga
#kelishi mumkin.


# import math #pythonni o'zida mavjud 'matematika' moduldan foydalanib ko'ramiz

# x=400
# print(math.sqrt(x))
# print(math.pow(5,3))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))

import random as r

# randint() #random modulidagi funksiya berilgan oraliqdagi 
# tasodifiy bir sonni generatsiya qilib qaytaradi (misoli pastda)

# son = r.randint(1,100)
# print(son)

# choise() #random modulidagi funksiya berilgan ro'yhatni ichidan 
# tasodifiy qiymatni tanlab olib, qaytaradi (misoli pastda)

# ismlar = ['shokir', 'botir', 'yusuf', 'mansur', 'ali', 'anvar']
# ism = r.choice(ismlar) #uzatiladigan ro'yhat bo'sh bo'lsa dastur xato qaytaradi
# print(ism)
# print(r.choice(ism)) # ro'yhatdan tanlab olingan qiymatni ichidan yana 
#                      # bir matnni tasodifiy tanlab qaytaradi.

# x = list(range(0,51,5)) # 0 dan 51 gacha bo'lgan sonlar ichidan 5 qadam
# print(x)
# print(r.choice(x))

#shuffle() - elementlarni aralashtirib tashlash uchun funksiyasi
x = list(range(11))
print(x)
r.shuffle(x)
print(x)




### bakhtiyor1308