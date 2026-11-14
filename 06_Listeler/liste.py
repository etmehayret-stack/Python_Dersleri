# urunler=["Kalemlik", "Saksı", "Aslan Biblo","Telefon Standı"]

# print(f"""
#       {urunler},
#       {urunler[0]},
#       {urunler[-1]}.
#       {len(urunler)}
      
#       {urunler[1]}.
#       {urunler[-2]}. 
      
      
#       """)

# urunler.append("Masa Lambası")

# print("\n".join(urunler),"\n")

# urunler.insert(1,"Telefon Tutucu")

# print("\n".join(urunler),"\n")

# urunler.extend(["Vazo","Duvar Saati"])

# print("\n".join(urunler),"\n")

# urunler.append(["Vazo", "Duvar Saati"])

# urunler.remove("Saksı")
# urunler.pop(-1)# urunler.pop() ta son elemanı siler


# urunler = ["Kalemlik", "Saksı", "Aslan Biblo", "Telefon Standı", "Vazo"]

# del urunler[0]

# for i in urunler:
#     print(i)
# print("\n")
    
# del urunler[1:3]

# for i in urunler:
#     print(i)
# print("\n")

# print(len(urunler))

# urunler.extend(["Kalemlik","biblo","onlar","bunlar","şunlar"])


# for i in urunler:
#     print(i)
    
# print(len(urunler))

# del urunler[5:]

# print(urunler)
# print(len(urunler))

# liste=urunler = ["Kalemlik", "Saksı", "Vazo", "Biblo", "Lamba", "Saat"]

# print(len(liste))

# del liste[0]

# print(len(liste))

# del liste[-2:]

# print(len(liste))

# for i in urunler:
#     print(i)

# liste = ["Kalemlik", "Saksı", "Vazo", "Saksı", "Biblo", "Saksı"]

# print(liste.count("Saksı"))

# print(liste.count("Vazo"))

# print(liste.count("Kalemlik"))

# print(liste.index("Kalemlik"))

# print(liste.index("Saksı"))

# urunler = [
#     "Kalemlik",
#     "Saksı",
#     "Vazo",
#     "Aslan Biblo",
#     "Masa Lambası"
# ]
# for i in urunler:
#     print(i)
# print("\n")
# del urunler[3]
# del urunler[:1]

# for i in urunler:
#     print(i)

# urunler = ["Vazo", "Kalemlik", "Saksı", "Aslan Biblo", "Masa Lambası"]

# urunler.sort()
# sorted(urunler)

# print(urunler)

sayilar=[3,5,7,9,2,8,1,6,10,4]

# sayilar.sort()

# print(sayilar)

# print(sorted(sayilar))


# sayilar.sort()

# sayilar.sort()

# for i in sayilar:
#     print(i)

# # sayilar.reverse()

# # for i in sayilar:
# #     print(i)

# sayilar.sort(reverse=True)

# for i in sayilar:
#     print(i)
    
# urunler = ["Kalemlik", "Saksı", "Vazo"]

# yeni_urunler = urunler
# yeni_urunler=urunler.copy()

# yeni_urunler.append("Lamba")



# print(urunler)
# print(yeni_urunler)
# print(len(urunler))

# print("Saksı"in urunler )
# print("Saksı"not in urunler )

# urunler = ["Kalemlik", "Saksı", "Vazo", "Lamba", "Aslan Biblo"]

# for i in urunler:
#     if "o" not in i:
#         print(i)


urunler= {
    "ürün adı": "Saksı",
    "fiyat": 150,
    "stok": 5,
    "renk": "Beyaz"
}

# for i in urunler:
#     print(i)
    
# for i in urunler.values():
#     print(i)   
     
# for i in urunler.items():
#     print(i)    
    
for anahtar, deger in urunler.items():
    print(anahtar, ":", deger)