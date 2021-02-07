from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib
import json
import requests
import json 
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


url="https://colombia.as.com/resultados/futbol/colombia_i/clasificacion/"
page=requests.get(url)
soup= BeautifulSoup(page.content,"html.parser")


#Equipos


eq= soup.find_all("span", class_="nombre-equipo")
equipos=list()
count= 0
for i in eq:
    if count < 19:
        equipos.append(i.text)
    else:
        break
    count +=1


#Puntos

pt= soup.find_all("td", class_="destacado")
puntos=list()
count= 0
for i in pt:
    if count < 19:
        puntos.append(i.text)
    else:
        break
    count +=1


escudo=list()
con=0
es= soup.find_all("span", class_="cont-img-escudo")
for element in es:
    ima=element.find("img").get("data-src")
    if con< 19:
        escudo.append(ima)
    else:
        break
    con +=1

print(escudo,len(escudo))

df= pd.DataFrame({"nombre":equipos,"puntos":puntos,"link":escudo})
js=df.to_json()

print(js)


app = Flask(__name__)

@app.route("/")
def server_info():
    cors = CORS(app, resources={"/*": {"origins": "*"}})
    idpok = request.args.get("id")

    var2=js
    return(var2)


if __name__=="__main__":
    app.run()