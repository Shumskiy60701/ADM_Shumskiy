import datetime
from modelsLab1 import *
import os


def createBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        os.remove('lab1.db')
        with db:
            db.create_tables([Client, Order])
    else:
        with db:
            db.create_tables([Client, Order])
        isfile = True
    return isfile

def fillBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        with db:
            clients = [
                {'Name': 'Emma Watson', 'City': 'New York', 'Address': '5th Ave, 123'},
                {'Name': 'Tom Hardy', 'City': 'London', 'Address': 'Baker St, 221B'},
                {'Name': 'Natalie Portman', 'City': 'Paris', 'Address': 'Champs-Élysées, 1'},
                {'Name': 'Idris Elba', 'City': 'Los Angeles', 'Address': 'Sunset Blvd, 666'},
                {'Name': 'Charlize Theron', 'City': 'Sydney', 'Address': 'Bondi Beach, 42'},
                {'Name': 'Chris Hemsworth', 'City': 'Melbourne', 'Address': 'Flinders St, 7'},
                {'Name': 'Gal Gadot', 'City': 'Tel Aviv', 'Address': 'Dizengoff St, 50'},
                {'Name': 'Ryan Reynolds', 'City': 'Vancouver', 'Address': 'Granville St, 777'},
                {'Name': 'Margot Robbie', 'City': 'Gold Coast', 'Address': 'Surfers Paradise, 33'},
                {'Name': 'Leonardo DiCaprio', 'City': 'Los Angeles', 'Address': 'Rodeo Dr, 90210'}
            ]
            Client.insert_many(clients).execute()
            clientss = Client.select()
            orders = [
                {'Client_id':clientss[0],'Date':datetime.date(2022,2,15),'Amount':1.0,'Description':'Table'},
                {'Client_id':clientss[1],'Date':datetime.date(2023,1,17),'Amount':4.0,'Description':'Boad'},
                {'Client_id':clientss[2],'Date':datetime.date(2021,7,22),'Amount':7.0,'Description':'Cup'},
                {'Client_id':clientss[3],'Date':datetime.date(2022,10,21),'Amount':10.0,'Description':'Hammer'},
                {'Client_id':clientss[4],'Date':datetime.date(2022,6,9),'Amount':14.0,'Description':'Nails'},
                {'Client_id':clientss[5],'Date':datetime.date(2023,2,19),'Amount':6.0,'Description':'Chair'},
                {'Client_id':clientss[6],'Date':datetime.date(2023,2,10),'Amount':9.0,'Description':'Fastener'},
                {'Client_id':clientss[7],'Date':datetime.date(2022,12,5),'Amount':1.0,'Description':'Lamp'},
                {'Client_id':clientss[8],'Date':datetime.date(2022,2,17),'Amount':16.0,'Description':'Screw'},
                {'Client_id':clientss[9],'Date':datetime.date(2023,1,1),'Amount':22.0,'Description':'Boad'}
            ]
            Order.insert_many(orders).execute()
        CheckForTable = True
    else:
        print("Базы данных не существует!")
    return CheckForTable

def showClientsBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        print(f"{'id' : <10}{'Name' : <15}{'City' : <15}{'Address' : <10}")
        for i in Client.select():
            print(f"{i.id : <10}{i.Name : <15}{i.City : <15}{i.Address : <10}")
    else:
        print("Базы данных не существует!")
    return Client.select().count()

def showOrdersBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        print(f"{'id' : <10}{'Client_id' : <14}{'Date' : <16}{'Amount' : <10}{'Description' : <10}")
        for i in Order.select():
            print(f"{i.id : <10}{i.Client_id}\t\t{i.Date}\t{i.Amount : <10}{i.Description : <10}")
    else:
        print("Базы данных не существует!")
    return Order.select().count()

if __name__ == "__main__":     
    print("Выберите желаемое действие\n1) инициализация\n2) заполнить\n3) отобразить TableName")
    task = input('Ваш выбор: ')
    if (task == '1'):
        createBD()
         
    if (task == '2'):
        fillBD()
        
    if (task == 'показать клиентов'):
        showClientsBD()

    if (task == 'показать заказы'):
        showOrdersBD()
