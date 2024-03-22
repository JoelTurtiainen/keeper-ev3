# Yleistä EV3DEV käytöstä
Ev3dev flashaaminen sd kortille:  
- https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/  

Tästä dokumentaatiosta löydät kaiken tarvittavan:  
- https://pybricks.com/ev3-micropython/  

Tietokoneen yhdistäminen laitteeseen:  
- https://www.ev3dev.org/docs/networking/  
- Laite tukee natiivisti bluetoothia, mutta wi-fi yhteys tarvitsee donglen usb porttiin.

### Hyvä tietää
- *LEGO® MINDSTORMS® EV3 MicroPython* Lisäosan mukana tulee valmiita ohjelmia joita voit testailla, tässä repossa on myös yksi esimerkki jonka tein esedun messuja varten.

- Jotkut metodit esim ```.straight()``` odottaa että ajaminen on loppunut, ennen kuin koodin suoritus jatkuu.

- Jos haluat tehdä muita asioita samalla käytä esim ```.drive()``` joka ajaa niin kauan kunnes robotti käsketään pysähtymään.

- Saat printtauksen näkymään 'Output' välilehteen jos olet yhdistänyt laitteen *ev3dev-browseriin*.

- Voit myös yhdistää laitteen SSH:lla ja tutkia laitteen käyttöjärjestelmää tai suorittaa komentoja *ev3dev-browser* avulla

- varmista että ohjelman alusta löytyy:  
```#!/usr/bin/env pybricks-micropython```

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

### VSCoden laajennukset:
https://marketplace.visualstudio.com/items?itemName=ev3dev.ev3dev-browser
https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython
