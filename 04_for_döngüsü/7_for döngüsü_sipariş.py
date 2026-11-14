import os
os.system("cls")
siparisler=[[101,420],[102,680],[103,225],[104,380]]
for i in siparisler:
    kargo=0 # burada tanımlanmayıp aşağıda if e  else kısmı eklenip yapılabilir
    kdvlifiyat=i[1]*1.2    
    if i[1] < 500:
        kargo=50       
    ödenecek=kdvlifiyat+kargo
    # print("sipariş no:",i[0],"| ürün fiyatı:",i[1],"| kdvli fiyat",kdvlifiyat,"| kargo ücreti: ",kargo,"|toplam ödenecek:",ödenecek) yerine aşağıdaki yazım daha sade görünüyor.
    print(f"sipariş no: {i[0]:<4} | ürün fiyatı: {i[1]:<4} | kdvli fiyat: {kdvlifiyat:<6} | kargo tutarı: {kargo:<3} | toplam ödenecek: {ödenecek:<6}")
    # : iki noktadan sonraki sayılar o veri için kaç hücre(hane) yer ayrılacağını belirler böylece sütun genişlikleri aynı yapılmış olur. < (Küçüktür İşareti): Veriyi sola yaslar (Metinlerin varsayılan davranışıdır).> (Büyüktür İşareti): Veriyi sağa yaslar (Sayıların varsayılan davranışıdır). ^ (Şapka İşareti): Veriyi tam ortalar. Sağına ve soluna eşit boşluk bırakır.Eğer boş kalan yerlerin boşluk karakteri yerine nokta (.) veya tire (-) ile dolmasını isterseniz, hizalama işaretinin hemen önüne o karakteri yazabilirsiniz:print(f"{i:.^10}")gibi

        
    
  
    
