from bs4  import BeautifulSoup
import requests
from Loco.models import Locomotive

url="https://en.m.wikipedia.org/wiki/Locomotives_of_India"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

tables = soup.findAll("table")
'''
0-Locomotive classification

1-Broad-gauge Electric Locomotives

2-Metre-gauge Electric Locomotives

3-Broad-gauge Diesel Locomotives

4-Metre-gauge Diesel Locomotives

5-Narrow-gauge Diesel Locomotives

6-Narrower-gauge Diesel Locomotives

7-Broad-gauge Dual Locomotives
'''
def saveLocomotive(Loco, data):
    Loco.motive_power = data[0]
    Loco.gauge = data[1]
    Loco.name = data[2]
    Loco.traction = data[3]
    Loco.usage = data[4]
    Loco.series = data[5]
    Loco.numbers = data[6]
    Loco.img_src = data[7]
    Loco.manufacturer = data[8]
    Loco.axles = data[9]
    Loco.numbers_built = data[10]
    Loco.production = data[11]
    Loco.power = data[12]
    Loco.status = data[13]
    Loco.save()

def getBroadElectric():
    for row in tables[1].tbody.find_all('tr')[1:]: #1:
        if(len(row)==2):
            continue

        columns = row.find_all('td')
        if(columns!=[]):
            if(len(columns)==10):
                norm = 0
                traction = columns[0].text.replace('\n','')
                usage = columns[1].text.replace('\n','')
            else:
                norm = 2
            motive_power = 'Electric'
            gauge = 'Broad'
            name = columns[2 - norm].text.replace('\n','')
            series = name[:4] if name[:3]=="WCA" else name[:3]
            numbers = "NA"
            img_src = "No Image Present"
            manufacturer = columns[4  - norm].text.replace('\n','')
            axles = columns[5  - norm].text.replace('\n','')
            numbers_built = columns[6  - norm].text.replace('\n','')
            production = columns[7  - norm].text.replace('\n','')
            power = columns[8  - norm].text.replace('\n','')
            status = columns[9  - norm].text.replace('\n','')

            data = [motive_power, gauge,name,usage,series,numbers,traction,
                    img_src, manufacturer,axles, numbers_built, production, power,status]
            Loco = Locomotive()
            saveLocomotive(Loco,data)
def getMeterElectric():
    for row in tables[2].tbody.find_all('tr')[1:]: 
        if(len(row)==2):
            continue

        columns = row.find_all('td')
        if(columns!=[]):
            traction = columns[0].text.replace('\n','')
            usage = columns[1].text.replace('\n','')
            motive_power = 'Electric'
            gauge = 'Meter'
            name = columns[2].text.replace('\n','')
            series = name[:3]
            img_src = "No Image Present"
            numbers = "NA"
            manufacturer = columns[4].text.replace('\n','')
            axles = columns[5].text.replace('\n','')
            numbers_built = columns[6].text.replace('\n','')
            production = columns[7].text.replace('\n','')
            power = columns[8].text.replace('\n','')
            status = columns[9].text.replace('\n','')

            data = [motive_power, gauge,name,usage,series,numbers,traction,
                    img_src, manufacturer,axles, numbers_built, production, power,status]
            Loco = Locomotive()
            saveLocomotive(Loco,data)

def getBroadDiesel():
    for row in tables[3].tbody.find_all('tr')[1:]:
        if(len(row)==2):
            continue

        columns = row.find_all('td')
        if(columns!=[]):
            if(len(columns)==10):
                norm = 0
                usage = columns[0].text.replace('\n','')
            else:
                norm = 1
            motive_power = 'Diesel'
            gauge = 'Broad'
            name = columns[1 - norm].text.replace('\n','')
            traction = "NA"
            series = name[:3]
            numbers = columns[2  - norm].text.replace('\n','')
            img_src = "No Image Present"
            manufacturer = columns[4  - norm].text.replace('\n','')
            axles = columns[5  - norm].text.replace('\n','')
            numbers_built = columns[6  - norm].text.replace('\n','')
            production = columns[7  - norm].text.replace('\n','')
            power = columns[8  - norm].text.replace('\n','')
            status = columns[9  - norm].text.replace('\n','')

            data = [motive_power, gauge,name,usage,series,numbers,traction,
                    img_src, manufacturer,axles, numbers_built, production, power,status]
            Loco = Locomotive()
            saveLocomotive(Loco,data)
def getNon_BroadDiesel(table,gauge_param):
    for row in table.tbody.find_all('tr')[1:]: #1:
        if(len(row)==2):
            continue

        columns = row.find_all('td')
        if(columns!=[]):
            if(len(columns)==9):
                norm = 0
                usage = columns[0].text.replace('\n','')
            else:
                norm = 1
            motive_power = 'Diesel'
            gauge = gauge_param
            name = columns[1 - norm].text.replace('\n','')
            series = name[:3]
            img_src = "No Image Present"
            manufacturer = columns[3  - norm].text.replace('\n','')
            axles = columns[4  - norm].text.replace('\n','')
            numbers_built = columns[5  - norm].text.replace('\n','')
            production = columns[6  - norm].text.replace('\n','')
            power = columns[7  - norm].text.replace('\n','')
            status = columns[8  - norm].text.replace('\n','')
            traction = "NA"
            numbers = "NA"
            data = [motive_power, gauge,name,usage,series,numbers,traction,
                    img_src, manufacturer,axles, numbers_built, production, power,status]
            Loco = Locomotive()
            saveLocomotive(Loco,data)
def getMeterDiesel():
    getNon_BroadDiesel(tables[4],"Meter")
def getNarrowDiesel():
    getNon_BroadDiesel(tables[5],"Narrow")
def getNarrowerDiesel():
    getNon_BroadDiesel(tables[6],"Narrower")

def getDualBroad():
    for row in tables[7].tbody.find_all('tr')[1:]:
        if(len(row)==2):
            continue

        columns = row.find_all('td')
        if(columns!=[]):
            if(len(columns)==9):
                norm = 0
                usage = columns[0].text.replace('\n','')
            else:
                norm = 1
            motive_power = 'Electric/Diesel'
            gauge = "Broad"
            name = columns[1 - norm].text.replace('\n','')
            series = name[:4]
            img_src = "No Image Present"
            manufacturer = columns[3  - norm].text.replace('\n','')
            axles = columns[4  - norm].text.replace('\n','')
            numbers_built = columns[5  - norm].text.replace('\n','')
            production = columns[6  - norm].text.replace('\n','')
            power = columns[7  - norm].text.replace('\n','')
            status = columns[8  - norm].text.replace('\n','')
            traction = "AC"
            numbers = "NA"
            data = [motive_power, gauge,name,usage,series,numbers,traction,
                    img_src, manufacturer,axles, numbers_built, production, power,status]
            Loco = Locomotive()
            saveLocomotive(Loco,data)