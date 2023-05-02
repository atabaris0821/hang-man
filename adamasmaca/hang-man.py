import turtle
import random
import requests
from bs4 import BeautifulSoup

ekran = turtle.getscreen()
mouse = turtle.Turtle()
harfler=""
dogru=0
deneme=5
kaçharfli=0 
url = "https://www.kelimetre.com/kelime-listeleri"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
isim =soup.find_all("li",{"class":"nokta"})
liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    liste.append([isim[i]])
#bir internet sitesinden yüzlerce türkçe kelime çektik
rastgele=random.choice(liste)
#çekilen yüzlerce kelimenin içinden rastgele bir kelime seçtik
asılkelime=rastgele
#print(rastgele)#/// kelimeler çok zor olduğu için denemek amacı ile kelime önceden görüntülenebilir.
kaçharfli=int(len(str(rastgele)))-4
#seçilen kelimenin kaç harfli olfuğunu bulduk
print("harf sayısı:",kaçharfli)
for x in range(kaçharfli):
    print("-",end="")
rastgele=str(rastgele)
rastgele=[*rastgele[2:]]
rastgele=[*rastgele[:-2]]
while deneme >= 1:
    tahminedilenharf=input("bir büyük harf gir: ")
    
    if tahminedilenharf in rastgele:
        print(f"\nTebrikler, tahmin ettiğiniz {tahminedilenharf} harfi gizli kelimenin içinde var") 
        dogru+=1        
    else:
        deneme-=1
        print(f"\nMaalesef tahmin ettiğiniz {tahminedilenharf} harfi gizli kelimenin içinde yok. {deneme} hakkın kaldı.")
        if deneme == 4:    
                #adam asma standı çizimi
            mouse.rt(90)
            mouse.fd(200)
            mouse.lt(90)
            mouse.fd(150)
            mouse.lt(180)
            mouse.fd(300)
            mouse.lt(180)
            mouse.fd(150)
            mouse.lt(90)
            mouse.fd(450)
            mouse.lt(90)
            mouse.fd(125)
            mouse.lt(90)
            mouse.fd(50)
                    
        elif deneme == 3:
            #Adam kafası çizimi
            mouse.rt(90)
            mouse.circle(50)
            mouse.lt(90)
            mouse.penup()
            mouse.fd(100)
            mouse.pendown()
            
        elif deneme == 2:
            #Adam gövdesi çizimi
            mouse.fd(175)
                  
        elif deneme == 1:
            #Adam bacakları çizimi
            mouse.goto(-225,-175)
            mouse.goto(-125,-75)
            mouse.goto(-25,-175)
            mouse.goto(-125,-75)
                
        elif deneme == 0:
            #Adam kolları çizimi
            mouse.rt(180)
            mouse.fd(125)
            mouse.goto(-225,0)
            mouse.goto(-125,50)
            mouse.goto(-25,-0)
            mouse.goto(-125,50)
            mouse.penup()
            mouse.home()
            
    harfler = harfler + tahminedilenharf
    for harf in rastgele:
        if harf in harfler:
            print(f"{harf}",end="")
            
        else:
            print("-",end="")
    if dogru >= int(len(set(str(rastgele))))-5:      
        print(f"Tebrikler, Kelimeyi Buldun. Adam asılmadan adamı kurtardın. Gizli kelime {asılkelime} idi")
if deneme == 0:
    print(f"Maalesef, gizli kelimeyi bulamadınız. Adam asıldı. kelime {asılkelime} idi")
    

