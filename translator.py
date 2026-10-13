import json,os,sys


language = "./config.json"      # Türkçe kelimeler ve kurallar,
words = "./words.json"   # Fransızca kelimeler ve kurallar,
ana_menü = ["Dil Seçin", "Kelime Arayın", "Çıkış"]

try:
    with open (language, "r", encoding="utf-8") as j_f:  #encoding="utf-8" kullanmamızın sebebi türkçedeki i,ü,ö gibi karakterleri aktarmak içindir.
        language = json.load(j_f)
except FileNotFoundError:
    print("config.json dosyası bulunamadı.\n")
try:
    with open (words, "r", encoding="utf-8") as j_f: 
        words = json.load(j_f)
except FileNotFoundError:
   print("words.json dosyası bulunamadı.\n")

def giriş1():
    global number
    print("Ana Menü")
    sayi1 = 1
    x = 0
    for giriş in ana_menü:
        print(f"{sayi1}-" , ana_menü[x])
        sayi1 += 1
        x += 1  
    try:
        number = int(input())
    except ValueError:
        number = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
    number = int(number)
    if number == 3:
            raise SystemExit
    while not 0 < int(number) < (len(ana_menü)+1) :
            number = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]: "))
    if number == 2:
        print("Lütfen önce dilleri seçiniz.")
    if number == 3:
        raise SystemExit

    
def bas_dil():
    global baslangic
    print("\nDiller Menü\nBaşlangıç dilinizi seçiniz")
    sayi2 = 1
    y = 0
    z = language.__getitem__("language") # Dictinory'nin içindeki istenilen değeri verir.
    for diller in z:
        print(f"{sayi2}-" , z[y])
        sayi2 += 1
        y += 1
    try:
        baslangic = int(input())     # İstenilen başlangıç dili seçer.
    except ValueError:  # Girilen verinin doğru yapıda olduğunu kontrol eder.
        baslangic = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
    baslangic = int(baslangic)
    while not 0 < int(baslangic) < len(z)+ 1:
        baslangic = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]: "))
    
def hedef_dil():
    global hedef
    print("\nHedef dilinizi seçiniz")
    sayi3 = 1
    y = 0
    z = language.__getitem__("language") # Dictinory'nin içindeki istenilen değeri verir.
    for diller in z:
        print(f"{sayi3}-" , z[y])
        sayi3 += 1
        y += 1
    try:
        hedef = int(input())     # İstenilen hedef dili seçer.
    except ValueError:
        hedef = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
    hedef = int(hedef)
    while not 0 < int(hedef) < len(z)+1:
        hedef = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]: "))
    while baslangic == hedef:
        print("Aynı iki dili çeviremezsiniz.\nLütfen başka bir dil seçiniz")
        hedef = str(input())
    
def giriş2():
    global number
    print("\nAna Menü")
    sayi4 = 1
    x = 0
    for giriş2 in ana_menü:
        print(f"{sayi4}-" , ana_menü[x])
        sayi4 += 1
        x += 1  
    try:
        number = int(input())
    except ValueError:
        number = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
    number = int(number)
    while not 0 < int(number) < len(ana_menü):
        number = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]: "))
    while number == 1:
        bas_dil()
        hedef_dil()
        sayi4 = 1
        x = 0
        print("\nAna Menü")
        for giriş2 in ana_menü:
            print(f"{sayi4}-" , ana_menü[x])
            sayi4 += 1
            x += 1  
        try:
            number = int(input())
        except ValueError:
            number = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
        number = int(number)
        while not 0 < int(number) < (len(ana_menü)+ 1):
            try:
                hedef = int(input())
            except ValueError:
                hedef = int(input("Lütfen geçerli bir sayı giriniz [1,2,3 gibi]:"))
        while number == 2:
            break
        
def kelime_arama():
    global hk, sonuç
    hk = input("Aradığınız kelimeyi giriniz: ").strip().lower() # İstenilen kelimenin boşluksuz ve küçül harflerle yazılmasını sağlar.
    if baslangic == 1 and hedef == 2:
        sonuç = next((kelime for kelime in words if kelime["Türkçe"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Ingilizce']}")
        else:
            print("Çeviri bulunamadı.")
    if baslangic == 1 and hedef == 3:
        sonuç = next((kelime for kelime in words if kelime["Türkçe"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Fransizca']}")
        else:
            print("Çeviri bulunamadı.")
    if baslangic == 2 and hedef == 1:
        sonuç = next((kelime for kelime in words if kelime["Ingilizce"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Türkçe']}")
        else:
            print("Çeviri bulunamadı.")
    if baslangic == 2 and hedef == 3:
        sonuç = next((kelime for kelime in words if kelime["Ingilizce"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Fransizca']}")
        else:
            print("Çeviri bulunamadı.")
    if baslangic == 3 and hedef == 1:
        sonuç = next((kelime for kelime in words if kelime["Fransizca"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Türkçe']}")
        else:
            print("Çeviri bulunamadı.")
    if baslangic == 3 and hedef == 2:
        sonuç = next((kelime for kelime in words if kelime["Fransizca"].lower() == hk), None)
        if sonuç:
            print(f"Sonuç: {sonuç['Ingilizce']}")
        else:
            print("Çeviri bulunamadı.")

def bit():
    global bitiş
    bitiş = str(input("Tekrar arama yapmak ister misiniz?(e/h):"))
    if str(bitiş.strip().lower) == "e":
        exit
    if str(bitiş.strip().lower) == "h":
        raise SystemExit      # Programı sonlandırır.
       
def ana_program():
    os.system('cls')      # Ekranı temizler. Önceden yapılan işlemler silinir.
    giriş1()
    bas_dil()
    hedef_dil()
    giriş2()
    if number == 3:
        raise SystemExit
    kelime_arama()
    bit()
    if bitiş == "e":
        os.system('cls')  # Ekranı temizler. Önceden yapılan işlemler silinir.
        return
    if bitiş == "h":
        raise SystemExit


while True:

    ana_program()
