
from datetime import datetime
from collections import UserDict
import re




class AddressBook(UserDict): #Клас для словника
    
#Метод запису заних до UserDict
    def add_record(self, data): #Метод для додавання словника до self.data
        super().update(data) #Додаю словник через super


#Метод для перевірки чи користувач є в словнику якщо є то виводить ім'я
    def find(self, fName): #Шукаю в словнику по імені
        try:
            return f"Find: {self.data[fName]}" #Повертаю результат
        except: return f"User -{fName}- is missing" #Повертаю попередження про відсутність користувача
    

#Метод видалення користувача
    def delete(self, dName): #Метод для видалення запису з словника 
        try: #Перевіряю на наявність користувача
            self.data.pop(dName) #Видаляю користувача
            print(f"Delet - '{dName}' ")
        except: print("User is missing") #Виводжу попередження що користувач відсутній
    
    
#Метод пошуку даних контактів користувача
    def find_contacts_user(self, contName, contValue):
        if self.data.get(str(contName)): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            userData = dict(self.data[contName])["contacts"] #Зберігаю словник користувача з UserDict і витягую з словника значення по ключу
            print(userData[contValue]) #Повертаю результат пошуку через прінт
            
        else: print(f"User -{contName}- is missing") #Повертаю попередження про відсутність користувача
    

#Метод пошуку даних користувача в UserDict
    def find_data_user(self, findValue, findName=None):
        if findName == None: #Якщо немає імені то виводжу всі вкладені значення з даних користувача
            
            for vl in self.data:  
                print(vl, self.data[vl][findValue]) #Виводжу всі значення з даних кожного користувача
        
        else: #Якщо є вхідне ім'я користувача то шукаю дані користувача
            if self.data.get(str(findName)): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
                userData = dict(self.data[findName])[findValue] #Зберігаю словник користувача з UserDict і витягую з словника значення по ключу
                return userData #Повертаю словник з даними користувача
            
            else: print(f"User -{findName}- is missing") #Повертаю попередження про відсутність користувача
    

#Метод пошуку тегів
    def find_tags_users(self, tagVal, tagNam):
        for tg in self.data: #Пробігаюсь циклом по словнику 
            if self.data[tg].get(tagVal): #Шукаю 'теги' в словниках користувачів
                dtu = str(dict(self.data[tg])[tagVal]) #Зберігаю знайдений тег з словника
                if tagNam == dtu: #Роблю перевірку за тегом
                    return print(dtu, tg) #Виводжу результат пошуку за тегом




#Метод додавання нових даних до користувача
    def add_data_to_users(self, dUser, newData, addNewData):
        if self.data.get(dUser): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            userData = dict(self.data[dUser]) #Зберігаю словник користувача з UserDict
            userData.update({newData: addNewData}) #Оновлюю словник користувача <- вхідним словником
            super().update({dUser: userData}) #Оновлюю словник користувача в UserDict
            print("Data has been updated")
    
    
    
#Метод для оновлення/додавання даних до користувача
    def update_user_contacts(self, uUser, uDat=None): #Оновлюю контактні дані користувача
        uDatKeys = "".join(dict(uDat).keys()) #Зберігаю ключ з вхідного словника який добавлю в контакти до користувача
        uDatValues = uDat[uDatKeys] #Зберігаю значення з вхідного словника
        phone_list = []
        if self.data.get(uUser): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            userD = dict(self.data[uUser]) #Зберігаю словник користувача з UserDict якщо є співпадіння    
            
            if userD.get("contacts"): #Якщо є співпадіння "contacts" то додаю дані
                contD = dict(userD["contacts"]) #Зберігаю словник "contacts" з користувача з UserDict
            
                if contD.get(uDatKeys) == None: #Якщо немає спіпадінь в словнику користувача то додаю новий словник до користувача 
                    contD.update(uDat) #Додаю значення до вкладеного словника в "contacts"
                    userD.update({"contacts": contD}) #Добавляю до словника "contacts" користувача <- вхідний словник
                    super().update({uUser: userD}) #Оновлюю користувача в UserDict
                    return print(f"'{uUser}' -> data has been added")
                
                if contD.get(uDatKeys): #Якщо є ключ в користувача то оновлюю значення словника
                    
                    if uDatKeys == "phone":
                        
                        for ph in contD[uDatKeys]:
                            if ph != None:
                                phone_list.append(ph)
                        phone_list.append(uDatValues)
                        contD.update({"phone": phone_list})
                    else:
                        contD.update(uDat) #Додаю значення до вкладеного словника в "contacts"
                        
                    userD.update({"contacts": contD}) #Добавляю до словника "contacts" користувача <- вхідний словник
                    super().update({uUser: userD}) #Оновлюю користувача в UserDict
                    return print(f"'{uUser}' -> data has been updated")
        
            else: print("Парамерт відсутній в контакті") #Можна реалізувати нові параметри до контакту
            
        else: return print(f"User '{uUser}' -> is missing") #Якщо користувача не знайдено
        
    
    
#Метод для оновлення/додавання нотаток користувача
    def add_notes_to_users(self, nUser, notes): #Приймає список [comentars , notate]
        comentars , notate = notes #Розбиваю вхідний список на змінні
        
        if self.data.get(nUser): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            contD = dict(self.data[nUser]) #Зберігаю словник користувача з UserDict якщо є співпадіння
            
            if contD.get("notes") != None: #Якщо є співпадіння "notes" то додаю нотатки
                noteD = dict(contD["notes"]) #Зберігаю словник "notes" з користувача з UserDict
                noteD.update({comentars: notate}) #Оновлюю словник з нотатками
                contD.update({"notes": noteD}) #Додаю нотатки до користувача
                super().update({nUser: contD}) #Оновлюю користувача в UserDict
                print("Нотатку додано")

            if contD.get("notes") == None: #Якщо в користувача немає нотаток
                inComent = {comentars: notate} #Створюю новий словник для нотаток
                contD.update({"notes": inComent}) #Додаю нотатки до користувача
                super().update({nUser: contD}) #Оновлюю користувача в UserDict
                print("Нотатку додано")

        else: return print(f"User '{nUser}' -> is missing") #Якщо користувача не знайдено
    

    
#Метод видалення даних користувача
    def delete_data_users(self, ddName, keyData, ddData=None): #Приймає ім'я, ключ для даних, дані(що видаляються) 
        if self.data.get(ddName): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            dataUser = dict(self.data[ddName]) #Зберігаю словник з даними користувача
            if ddData == "all": #Команда для видалення всіх нотаток
                print(dataUser.pop(keyData)) #Видаляю словник з нотатками
                super().update({ddName: dataUser}) #Оновлюю користувача в UserDict
            else:
                try:
                    print("delet->", ddData, "-", dataUser[keyData].pop(ddData)) #Видаляю дані користувача
                except: return print(f"User {ddName} note is missing") #Попередження про відсутність нотатки в користувача
                
        else: return print(f"User '{ddName}' -> is missing") #Якщо користувача не знайдено
    


#Метод для виведення днів народження на наступний тиждень (на задану кількість днів)
    def find_birthday_users_for_week(self): # birthdays
        try:
            today_time = datetime.today().date() #Зберігаю поточну дату
            dict_res = {} #Словник для результату пошуку
            
            for ur in self.data: #Проходжусь по словнику UserDict
                users_dicts = dict(self.data[ur])["contacts"] #Зберігаю словник користувача
                # print(users_dicts)
                
                if users_dicts.get("birthday"): #Роблю перевірку наявність дати народження
                    birtDT = datetime.strptime(users_dicts["birthday"], '%Y-%m-%d').date() #Перетворюю ДН з словника в об'єкт datetime
                    repYear = birtDT.replace(year=today_time.year) #Замінюю рік з ДН на поточний
                    
                    res_bird = int(( repYear - today_time ).days) #Віднімаю ДН від поточної дати і зберігаю як int
                    if res_bird <= 7 and res_bird >= 0: #Перевіряю чи на цьому тижні ДН
                        dict_res.update({ur: birtDT.isoformat()}) #Додаю до словника результатат перевірки 
                        
            return dict_res #Повертаю словник з результатом пошуку
        
        except: print("Wrong date in the dictionary") #Виводжу повідомлення якщо є помилкова дата народження в словнику
    
    






class Field(): #Базовий клас поля для контакту
    def __init__(self, fd_Name, fd_Phone=None) -> None:
        self.fd_Name = fd_Name
        self.fd_Phone = fd_Phone


class Name(Field): #Клас для імені 
    def __init__(self, valName) -> None:
        self.valName = valName        
    
    def __str__(self) -> str:
        return self.valName


class Phone(Field): #Клас для телефону
    def __init__(self, valPhone) -> None:
        self.valPhone = valPhone
    
    def phone_validation(self): #Валідація номеру телефону
        if isinstance(self.valPhone, str) and len(self.valPhone) == 13 and self.valPhone.startswith("+380"): #Перевірка номера телефону
            return self.valPhone #Повертаю перевірений телефон
        else: return print("Wrong phone format")


class Birthday(Field): #Клас для дати народження
    def __init__(self, valBirthday):
        self.valBirthday = valBirthday
    
    def birthday_validation(self): #Валідація дати народження
        try:
            validBirt = "".join(re.findall("\\d{2}\\.\\d{2}\\.\\d{4}", self.valBirthday)) #Додаю до рядка результат пошуку елементів врядку 
            self.lBirthday = datetime.strptime(validBirt, '%d.%m.%Y').date() #Пробую перетворити ДН з словника в об'єкт datetime
            return self.lBirthday.isoformat() #Повертаю об'єкт datetime з методом isoformat()
        
        except ValueError: 
            raise ValueError("Invalid date format. Use DD.MM.YYYY") #Виводжу помилку


class Email(Field): #Валідація пошти-----------------------------
    def __init__(self, valEmail):
        self.valEmail = valEmail
        print(self.valEmail)
    
    def email_validation(self):
        email_regex = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #--------------------------------
        if re.match(email_regex, self.valEmail):
            return self.valEmail #Вертаю почту
        else: raise ValueError("Invalid Email") #Вертаю помилку



class Record: #Шаблон користувача
    
    """Клас `Record` для зберігання інформації про контакт
    Типу форма для словника
    Можна вказати додаткові
        обов'язкові параметри до контакту
        які будуть записуватись в AddressBook
    """
        
    def __init__(self, name):
        self.name = name #Зберігаю обєкт імені
        self.phones = None #Список для телефонів
        self.birthday = None #День народження
        self.dictREC = {} #Вихідний словник
    
    def dict_record(self): #Метод для створення словника
        self.dictREC = {self.name: { #Записую в словник
            "contacts": {
                "phone": [self.phones],
                "birthday": self.birthday
                },
            "notes": {
                'Note1': 'Hello',
                'Note2': 'World',
            }
            }}
        return self.dictREC #Вертаю словник


