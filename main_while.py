
# Khayitov Bakhtiyor
# 05/10/2021 23:01


### INPUT() va While

#son = 1
#while son <= 4:
#    print(son, end=' ')
#    son += 1
#print("Dastur tugadi!")

#temperature = 115
#while temperature > 112:
#    print(temperature)
#    temperature -= 1

#print('The tea is cool enough.')

#  #  # while and input
#print('Kiritilgan sonning kvadratini chiqaruvchi dastur.')
#savol = 'Istalgan son kiriting.'
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)

#print("Dastur tugadi!")

#  #  # ishora
#print('Kiritilgan sonning kvadratini chiqaruvchi dastur.')
#savol = 'Istalgan son kiriting.'
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
#print("Dastur to'xtadi!")

#  #  # break while
#print('Kiritilgan sonning kvadratini chiqaruvchi dastur.')
#savol = 'Istalgan son kiriting.'
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break  # tsiklni to'xtatish
#    else:
#        print(float(qiymat)**2)
#print("Dastur to'xtadi!")

#  #  # break for
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng.")

#  #  # Continue for
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue # 5 sonining kvadratini chiqarmasdan tsikl shartini boshiga qaytib, jarayon davom ettiriladi
#    print(f"{son} ning kvadrati {son**2} ga teng.")

#  #  # Continue while
#son = 0
#while son<10:
#    son += 1
#    if son%2!=0: # juft sonlarni chiqaradi
#        continue
#    else:
#        print(son)

#son = 0
#while son<10:
#    son += 1
#    if son%2==0:  # toq sonlarni chiqaradi
#        continue
#    else:
#        print(son)

# # # infinite loop (dastur bajarilishida tsikl to'xtamasdan takrorlanib turaveradi)
#son = 0
#while son<10:
#    if son%2!=0:
#        continue
#    else:
#        print(son)


### bakhtiyor1308