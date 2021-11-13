
# Khayitov Bakhtiyor
# 26/10/2021 17:46

# # # MAVZU: FUNKSIYADAN QIYMAT QAYTARISH

#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism

#talaba1 = toliq_ism_yasa('botir','zokirov')
#talaba2 = toliq_ism_yasa('shokir','alimov')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}.")
#print(f"{talaba1} kechagi darsga ham kelmagan edi.")

#def toliq_ism_yasa ( ism , familiya, otasining_ismi='') :
#    """To'liq ism qaytaruvchi funksiya"""
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()

#talaba1 = toliq_ism_yasa('botir','zokirov')
#talaba2 = toliq_ism_yasa('shokir','alimov', 'komilovich')

#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}.")

#def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rang':rangi,
#            'korobka': karobka,
#            'yil':yili,
#            'narh':narhi}
#    return avto

#avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
#avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)

#print(avto1) #--bu yerda avto1 haqidagi to'liq ma'lumotlar qaytariladi
#print(avto1['model']) #--bu yerda avto1 modeli haqidagi ma'lumot qaytariladi
#print(avto1['narh']) #--bu yerda avto1 narhi haqidagi ma'lumot qaytariladi
#print(avto2['narh']) #--bu yerda avto2 narhi haqidagi ma'lumot qaytariladi

#avtolar = [avto1, avto2]
#print(avtolar)
#print(avtolar[0]['model'])
#print("Onlayn bozordagi mavjud avtomashinalar:")
#for avto in avtolar:
#    if avto['narh']:
#        narh = avto['narh']
#    else:
#        narh = "Noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#def oraliq(min,max):
#    sonlar = []
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar

#print(oraliq(0,10))
#print(oraliq(10,21))

def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka': karobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yhatini shakllantiramiz!")
avtolar = [] #salondagi avtolar uchun bo'sh ro'yhat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end=' ')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    karobka=input("Karobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    #Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
    #lug'at shakllantirilib, har bir lug'atni ro'yhatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
    #Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break

print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {karobka} karobka. Narhi: {narh}")



print(avtolar)




### bakhtiyor1308