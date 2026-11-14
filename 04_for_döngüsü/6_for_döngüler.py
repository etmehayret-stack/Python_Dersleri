import os
os.system("cls")
sayilar=[1,2,3,4,5,6,7,8,9,10]
for i in sayilar:
    print(i*i)
    print(i**2)
for i in range(10):#sıfırdan başlar on sayı üretir
    print(i)#bunu doğrudan bir liste olarak tanımlamak istersek list()fonksiyonu ile kullanmalıyız.
liste=list(range(10))
print(liste)
for i in liste:
    print(i**2)#aynı işi liste oluşturmadan 
for i in range(10):# TEK PARAMETRELİ(sıfırdan başla 10 hariç e kadar birer )
    print(i**2)#şeklinde de yapabiliriz.
for i in range(5,18):# İKİ PARAMETRELİ (5 ten başla 18 hariç e kadar birer)
    print(i)
for i in range(15,96,3):# ÜÇ PARAMETRELİ (15 ten başla 96 ı hareç e kadar üçer üçer)
    print(i)
for i in range(100,45,-5):# ÜÇ PARAMETRELİ (15 ten başla 96 ı hareç e kadar üçer üçer)
    print(i)#96 dan başla 15hariç e kadar eksi üçer eksi üçer)
for i in range(100,-45,-5):
    print(i)
for i in range(11):
    if i%2==0:
        print(i**2)
for i in range(1,11):
    #print(i)
    for ii in range(1,i+1):
        print(f"{i} x {ii} = {i * ii}")
    print()
for i in range(1,11):
    print(i*"*")
for i in range(1,6):
    for ii in range(1,i+1):
        print(ii,end="")
    print()

for i in dolap:
    print(i)
dolap=["gömlek", "pantolon", "ceket", "tişört"]
for i,ii in enumerate(dolap,start=1):# i sırasını ii adını temsil eder burada start ilk ürüne kaç numarası verilsin diye sorar diğerleri ona göre sırayla gider.
    print(i,ii)

yorum=["Harika", "Çok iyi", "Kötü", "Muhteşem"]#yasaklı kelimeyi bulduğunda Döngüyü tamamen patlatır/bitirir.
for i in yorum:
    if i=="Kötü":
        print(f'yasaklı kelime "{i}" bulundu') 
        print(f"yasaklı kelime '{i}' bulundu") 
        print('yasaklı kelime "'+i+'" bulundu') 
        print("yasaklı kelime '"+ i +"' bulundu") 
        print('yasaklı kelime "',i,'" bulundu') 
        print("yasaklı kelime '", i ,"' bulundu")   
        break
else:
    print("yasaklı kelimeye rastlanmadı")
sepet=["Süt", "Ekmek", "Poşet", "Yumurta"]#poşeti atlayıp diğerlerini yazdırır
for i in sepet:
    if i == "Poşet":
        continue
    print(i)
