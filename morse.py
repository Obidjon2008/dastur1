# def to_morse(soz):
#     l = {
#         'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
#         'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
#         'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
#         'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
#         'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--',
#         'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
#         '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
#         '0':'-----'
#     }
#
#     code = ''
#     soz = soz.lower()
#     for i in soz:
#         code += l[i]
#         code += '/'
#
#     return code
#
#
#
# to_morse('assalom')
# print("Hech qanday qiymat qaytarmaydi")
# print(to_morse("salom"))
# print("Bunisi qiymat qaytaradi")


# def daraja(son1, son2): # def bulderi yordamida son1 va son2 argumentlariga ega daraja deb nomlangan funksiya hosil qilindi
#     return son1**son2 # son1 ni son2 darajaga oshirib qiymatini funksiyaga qaytardi
#
#
# a = daraja(3, 6)  # daraja funksiyasi chaqirilib unga argumentlar berildi va undan qaytayorgan qiymat a o`zgaruvchiga yuklandi
# print(a) # a o`zgaruvchisi ekranga chiqarildi


# def yigindi(toplam):
#     s = 0
#     for i in toplam:
#         if str(i).isdigit():
#             s += i
#
#     return s
#
# raqamlar = [1, 2, 3, 4, 5, 'abdulaziz', 6, 7, 8, 9, 'salom']
#
# summa = yigindi(raqamlar)
# print(summa)

#
# def top(argument1, argument2):
#     l = []
#     for i in argument2:
#         if i in argument1:
#             l.append(i)
#
#     return l
#
# # print(top("abc", 'bdc'))
# n=int(input())
# massiv=[]
# for _ in range(n+1):
#   s = int(input())
#   massiv.append(s)
# massiv.sort()
# for item in massiv:
#     print(item)
# a = int(input())
# b = list(map(int, input().split()))
# c = int(input())
# d = b.count(c)
# print(d)

# a = int(input())
# l = {
#     1:'bir',
#     2:'ikki',
#     3:'uch',
#     4:'to`rt',
#     5:'besh',
#     6:'olti',
#     7:'yetti',
#     8:'sakkiz',
#     9:'to`qqiz',
#
#
# }
# l1 = {
#     0: '',
#     10: 'o`n',
#     20:'yigirma',
#     30:'o`ttiz',
#     40:'qirq',
#     50:'ellik',
#     60:'oltmish',
#     70:'yetmish',
#     80:'sakson',
#     90:'to`qson'
# }
# birlar = a%10
# onlar = a-birlar
#
# print(f'{l1[onlar]} {l[birlar]}')
# 
# s = input()
# ik = s.count('2')
# uc = s.count('3')
# tor= s.count('4')
# besh = s.count('5')
# yet = s.count('7')
# if ik>0 or uc>0 or tor>0 or besh>0 or yet>0:
#   print('NO')
# else:
#   l = {
#   	'0':'0',
#     '1':'1',
#     '6':'9',
#     '8':'8',
#     '9':'6'
#   }
#   s1 = ''
#   s = list(s)
#   s.reverse()
#   s2 = ''
#   for i in s:
#       s2+=i
#   for i in s2:
#     s1 += l[i]
#   if s == s1:
#   	print('YES')
#   else:
#     print('NO')


# sinf = {
#   'Yodgor': {
#     'familiya': 'Xusanov',
#     'yosh': 15,
#     'manzil': 'Bo`ston'
#   },
#
#   'Abdulaziz': {
#     'familiya': 'Islomov',
#     'yosh': 14,
#     'manzil': 'Ozod'
#   },
#
#   'Izzatillo': {
#     'familiya': 'Adhamov',
#     'yosh': 15,
#     'mazil': 'Eskiqo`rg`on'
#   }
# }
# yoshlar = []
#
#
# for i in sinf:   #sinf lugatini har bir elementi uchun
#   yoshlar.append(sinf[i]['yosh']) #yoshlar toplamiga elementni yosh kalitining qiymatini qoshadi
# y = min(yoshlar) #yoshlar toplamini eng kichik qiymartini topadi
# for i in sinf: #sinfdagi har bir element uchun
#   if sinf[i]['yosh'] == y: #agar elementni yoshi y ga teng bolsa
#     print(i) #osha elementni chiqarib beradi

# pitsa_dokon = {
#   'turi':{
#     'katta':5,
#     'orta':3,
#     'kichik':2
#   },
#   'masalliq':{
#     'sir':2,
#     'sabzavot':3,
#     'gosht':1
#   },
#   'bezak':{
#     'pomidor':0.5,
#     'qoziqorin':0.3,
#     'mayonez':0.1
#   }
# }
#
# narx = 0
# zakaz = input('Pitsa markazimizga hush kelibsiz.\nBirir nima buyurtma qilasizmi?(ha/yoq): ').lower()
# if zakaz == 'ha':
#   while True:
#     turi = input('Pitsa turini tanlang(katta/orta/kichik): ').lower()
#     if turi in list((pitsa_dokon['turi']).keys()):
#       narx += pitsa_dokon['turi'][turi]
#       break
#     else:
#       print('Bizda unday maxsulot turi yo`q')
#   while True:
#     maxsulot = input('Masalliqni tanlang(sir/sabzavot/gosht): ').lower()
#     if maxsulot in list((pitsa_dokon['masalliq']).keys()):
#       narx += pitsa_dokon['masalliq'][maxsulot]
#       break
#     else:
#       print('Bizda unday masalliq turi yo`q')
#   while True:
#     bezak = input('Bezak turini tanlang(pomidor/qoziqorin/mayonez): ').lower()
#     if bezak in list((pitsa_dokon['bezak']).keys()):
#       narx += pitsa_dokon['bezak'][bezak]
#       break
#     else:
#       print('Bizda unday masalliq turi yo`q')
#
# print(f'Szidan {narx} dollar boldi')


def sontop():
  import random
  daraja_l = {
    'oson': 10,
    'qiyin':5
  }
  daraja = input('Qiyinchilikni tanlang(oson/qiyin): ').lower()
  urunishlar = daraja_l.get(daraja)
  rSon = random.randint(1, 101)
  print(f'Men 1 dan 100 gacha bir son o`yladim va siz buni {urunishlar} ta urinish bilan topishingiz kerak')
  sanoq = 0
  print(rSon)
  while sanoq != urunishlar:
    javob = int(input('Son'))
    if javob == rSon:
      print('togri siz yutdingiz')
      break
    else:
      print('xato')
      if javob>rSon:
        print('Men oylagan son kichikroq')
      elif javob<rSon:
        print('Men oylagan son kattaroq')
      sanoq += 1
    if sanoq == urunishlar:
      print('Siz maglub boldiz')
      break



sontop()