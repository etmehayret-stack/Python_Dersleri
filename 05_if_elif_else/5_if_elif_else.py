import os
os.system("cls")
dnot=input("Ders notunu gir:")
if dnot.isdigit() :
    dnot=int(dnot)
    if -1<dnot<101:        
        if dnot>=85:
            print("5 oldın ")
        elif 75<=dnot<85:
            print("4 aldın")
        elif 55<=dnot<75:
            print("3 aldın")
        elif 45<=dnot<55:
            print("2 aldın ucundan yırttın")
        else:
            print("ders notun 45 in altında olduğu için sınıfta kaldın")
    else:
        print("1 ile 100 arasında bir değer gir")
        

else:
    print("sayısal bir değer gir")
