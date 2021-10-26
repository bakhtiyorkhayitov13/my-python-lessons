
# Khayitov Bakhtiyor
# 25/10/2021 17:40

# # # MAVZU: FUNCTIONS (FUNKSIYALAR)

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum!")

#salom_ber()

##funksiya foydalanuvchidan nomini so'rab, nomi bilan salom beruvchi funksiya yaratamiz

#def salom_ber(ism): # bu yerda ism so'zi funksiya parametri deb ataladi
#    """foydalanuvchini ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

#salom_ber('hasan')
#salom_ber('olim')

#print(salom_ber.__doc__) # salom_ber() funksiyasi haqida ma'lumot olish
#print(print.__doc__) # print() funksiyasi haqida ma'lumot olish

## yana bir misol
#def toliq_ism(ism, familiya):
#    """foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}.\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}.")

#toliq_ism('olim', 'hakimov')
# toliq_ism('hakimov', 'olim') # bu misolda familiya bilan
# ism o'rni almashgan holda tushunarsiz ma'lumot chiqadi.


#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2021-tugilgan_yil} yoshda.")

#yosh_hisobla('olim',1991)
#yosh_hisobla(1991,'olim') #o'rin almashgan, xato variant

#yosh_hisobla(tugilgan_yil=1991, ism='olim') #yoki
#yosh_hisobla(ism='olim', tugilgan_yil=1991) # ikkala variantda ham natija bir xil chiqadi

#toliq_ism(familiya='hakimov', ism='olim')

#pastda standart qiymat kiritish usulini o'rganamiz

def yosh_hisobla(tugilgan_yil, joriy_yil=2021): #bu yerda joriy yilga standart qiymat kiritmasak, dastur xatolik beradi
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")

#yosh_hisobla(1991,2021)
#yoki
yosh_hisobla(1991)







### bakhtiyor1308