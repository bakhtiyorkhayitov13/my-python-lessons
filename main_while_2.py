
# Khayitov Bakhtiyor
# 06/10/2021 15:29


# # # MAVZU: While ro'yhatlar va lug'atlar



## RO'YHATDAN FOYDALANISH
#print("Yaqin do'stlaringiz ro'yhatini tuzamiz.")
#ismlar = []
#n=1     #ismlarni sanash uchun o'zgaruvchi
#while True:
#    savol = f"{n}-do'stingiz ismini kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#        break

#print("Do'stlaringiz ro'yhati: ")
#for ism in ismlar:
#    print(ism.title())



## LUG'ATDAN FOYDALANISH
#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingizning ismini kiriting: ")
#    yosh = input(f"{ism.title()}ning yoshini kiriting:")
#    dostlar[ism] = int(yosh)

#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False

#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#print(dostlar)



## WHILE TSIKLI YORDAMIDA RO'YHATDAGI QIYMATLARNI O'CHIRISH
#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars:
#    cars.remove('nexia')    # .remover() metodi aslida ro'yhatda bir nechta marta takrorlangan elementni fataq 1-turganini o'chirib tashlaydi.
                            # biz bu jarayonni bir necha marta takrorlab o'tirmaslik uchun "while" tsiklidan foydalanamiz.

#print(cars)
## yana bir usuli (osonroq variant)
#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#car = 'lacetti'
#while car in cars:
#    cars.remove(car)    # .remover() metodi aslida ro'yhatda bir nechta marta takrorlangan elementni fataq 1-turganini o'chirib tashlaydi.
                            # biz bu jarayonni bir necha marta takrorlab o'tirmaslik uchun "while" tsiklidan foydalanamiz.

#print(cars)

##boshqa misolni ko'ramiz
talabalar = ['ali', 'vali', 'odil', 'sobir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = int(baho)

print(talabalar)
print(baholangan_talabalar)


### bakhtiyor1308