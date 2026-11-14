a="elma","armut"
b=("elma","armut")
print(a)
print("a nın tipi : ",type(a))
print("b nın tipi : ",type(b))


import os
os.system("cls")
s1=2
s2=8
s3=None

l1="elma,armut,üzüm"
l2=["elma","armut","üzüm"]
l3=("elma","armut","üzüm")
sö1={"ad":"Hayrettin","Soyad":"Toroman","Yaş":"25"}
k1={"elma","Hayrettin","Soyad","elma","Yaş","25","25","Hayrettin","Soyad","armut","Yaş","25"}

print("1. sayı :",s1)
print("2. sayı :",s2)
print("3. sayı :",s3)
print("1. liste :",l1)
print("2. liste :",l2)
print("3. liste :",l3)
print("1. sözlük :",sö1)
print("1. küme :",k1)

print()
print("toplamları :",s1+s2)
print("farkları :",s1-s2)
print("çarpımları :",s1*s2)
print("birbirine bölümü :",s1/s2)
print("tam sayılı bölümleri :",s1//s2)
print("1. sayının karesi :",s1**2)
print("1. sayının küpü :",s1**3)
print("1. sayının 2. sayı cinsinden üssü :",s1**s2)
print("1. sayının 2. sayıya bölümünden kalan :",s1%s2)
print("2. sayının 1. sayıya bölümünden kalan :",s2%s1)
print("2. sayının 5 e sayıya bölümünden kalan :",s2%5)
print("100 ün 13 e bölümünden kalan :",100%13)
print("8 ün 5 e bölümünden kalan :",8%5)
print("1. sayı 2. sayıdan büyükmüdür :",s1>s2)
print("3. sıyının içi boşmudur :",s3 is None)
print()
print("1. sayının tipi :",type(s1))
print("2. sayının tipi :",type(s2))
print("3. sayının tipi :",type(s3))
print("1. listenin tipi :",type(l1))
print("2. listenin tipi :",type(l2))
print("3. listenin tipi :",type(l3))
print("1. sözlüğün tipi :",type(sö1))
print("1. kümenin tipi :",type(k1))

print()
print("toplamlarının sayının tipi :",type(s1+s2))
print("farklarının tipi :",type(s1-s2))
print("çarpımlarının tipi :",type(s1*s2))
print("bölünmelerinin tipi :",type(s1/s2))
print("tam sayı bölünmelerinin tipi :",type(s1//s2))
print("büyüklük karşılaştırması tipi :",type(s1>s2))
print("3. sayının içi boşmu sorgulamasının tipi :",type(s3 is None))

