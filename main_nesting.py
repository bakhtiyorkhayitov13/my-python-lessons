
# Khayitov Bakhtiyor
# 04/10/2021 16:00


### Nesting

car0 = {
    'model':'kia',
    'colour':'white',
    'year':2018,
    'cost':15000,
    'kilometers':30000,
    'transmission':'automate'
    }

car1 = {
    'model':'tesla',
    'colour':'green',
    'year':2020,
    'cost':50000,
    'kilometers':10000,
    'transmission':'automate'
    }

car2 = {
    'model':'nexia 3',
    'colour':'red',
    'year':2019,
    'cost':10000,
    'kilometers':6000,
    'transmission':'mechanical'
    }

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['colour']} colour, "
          f"{car['year']}-year, {car['cost']}$")

# Eslatma: yuqoridagi usulda boshqalariga nisbatan yozgan kodimiz uzun bo'lib ketmaydi.

#print(type(cars))
print(cars) #cars ro'yhatidagi hamma ma'lumotlarni chiqarish

print(cars[0]) #cars ro'yhatidagi 0-element(lug'at)ni chiqaramiz

print(cars[0]['model']) #cars ro'yhatidagi 0-element(lug'at)ni ichidagi model qiymatini chiqaramiz
print(cars[1]['colour']) #cars ro'yhatidagi 1-element(lug'at)ni ichidagi colour qiymatini chiqaramiz

#for tsiklidan foydalanish

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'colour':None, #rangi noaniq
        'year':2020,
        'cost':None,
        'kilometers':0,
        'transmission':'automate'
        }
    malibus.append(new_car)

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[:3]:
    malibu['colour']='red'

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[3:6]:
    malibu['colour']='black'

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[6:]:
    malibu['colour']='white'
    malibu['transmission'] = 'mechanical'

#for malibu in malibus:
#    print(malibu)

for malibu in malibus:
    if malibu['transmission']=='automate':
        malibu['cost']=40000
    else:
        malibu['cost']=35000

for malibu in malibus:
    print(malibu)

#Lug'at ichida ro'yhat
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(f"{til.upper()} ", end='')

hamkasblar = {
    'hasan':{'familiya':'aliyev',
             't_yil':1990,
             'malumot':"o'rta maxsus",
             'tillar':['python', 'c++']
            },
    'husan':{'familiya':'choriyev',
             't_yil':1988,
             'malumot':"o'rta maxsus",
             'tillar':['html', 'css', 'js']
            },
    'umar':{'familiya':'olimov',
             't_yil':1992,
             'malumot':"maxsus",
             'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidafi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())

# mustahkamlash uchun mashqlar...
davlatlar = {
    'amerika':{'tuzumi':'qoshma shtatlari',
            'qita':'amerika',
            'tili':'ingliz',
            'prezident':'bayden'
            },
    'rossiya':{'tuzumi':'federatsiya',
                'qita':'yevropa',
                'tili':'rus tili',
                'prezident':'putin'
            },
    'uzbekistan':{'tuzumi':'respublika',
                'qita':'osiyo',
                'tili':'uzbek tili',
                'prezident':'mirziyoyev'}
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()} {info['tuzumi'].title()}, "
          f"{info['qita']}-qitasida joylashgan. "
          f"Davlat tili: {info['tili'].title()}. \n"
          f"Davlat rahbari: {info['prezident'].title()}. ")

# quyidagi mashqda foydalanuvchidan davlat nomini kiritish so'raladi.
# Agar davlat lug'atda mavjud bo'lsa consolga kiritilgan davlat haqidagi ma'lumotlar chiqadi.
# Aks holda bo'lsa, consolga Bizda bu davlat haqida ma'lumot mavjud emas degan javon chiqadi.

davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.title()} {info['tuzumi'].title()}, "
          f"{info['qita']}-qitasida joylashgan. "
          f"Davlat tili: {info['tili'].title()}. \n"
          f"Davlat rahbari: {info['prezident'].title()}. ")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas.")



### bakhtiyor1308