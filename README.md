# keeper-ev3
## LEGO EV3 Robotti joka etsii pallon ja nappaa sen 

>[!NOTE]
>Ohjelma on tarkoitettu robotille joka käyttää [LEGO:n ohjeiden](https://education.lego.com/en-us/product-resources/mindstorms-ev3/downloads/building-instructions/) mukaan tehtyjä:  
-Driving Base  
-Color Sensor Down  
-Medium Motor Driving Base  
-Ultrasonic Sensor Driving Base

# Yleistä EV3DEV käytöstä
### Tästä dokumentoinnista löydät kaiken vaadittavan oman projektin luomiseen:  
https://pybricks.com/ev3-micropython/
### Tietokoneen yhdistäminen laitteeseen:
https://www.ev3dev.org/docs/networking/  
Laite tukee natiivisti bluetoothia, mutta wi-fi yhteys tarvitsee donglen usb porttiin.
### Hyvä tietää
1. Jotkut metodit esim ".straight()" odottaa että ajaminen on loppunut, ennen kuin koodin suoritus jatkuu.
- Jos haluat tehdä muita asioita samalla käytä esim ".drive()" joka ajaa niin kauan kunnes auto saa uuden komennon

print komento myös toimii normaalisti ja näät tulostuksen terminaalin 'output' välilehdestä

# Importtien tuominen
>[!TIP]
>Jos haluat asentaa pip paketin vain projektille, luo **venv**.  
>(Voit käyttää vanhaa venv sijaintia jos olet jo luonut sen)


### Venv:in luominen

VSCoden oikeasta alakulmasta.
```
'Intepreter'

'Create Virtual Environment'

'Venv'

'Python 3..."
```

  
### Pybricks paketin tuominen  
https://pypi.org/project/pybricks/2.0.0.post2/  

```
pip install pybricks==2.0.0.post2
```
### vscode/settings.json:
```
"python.languageServer": "Pylance"
```
