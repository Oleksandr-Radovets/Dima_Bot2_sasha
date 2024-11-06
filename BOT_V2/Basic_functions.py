
import pickle
import Address_Book #Імпортую свій файл з користувачами


""" Функції """
def all_book(User_book:Address_Book) -> str:
    """Функція виведення контактів"""
    for b in User_book.data:
        print(b, User_book[b])
        

def add_user_book(addUser, User_book:Address_Book) -> str: 
    """
    Функція
    додавання користувача до UserDict
    """
    u = "".join(addUser) #Додаю ім'я зі списку до рядка
    if u: #Роблю перевірку на пусте значення
        rec = Address_Book.Record(u) #Створюю об'єкт класу Record
        User_book.add_record(rec.dict_record()) # І записую в UserDict
        print(f"Сontact '{u}' added")
    else: print("!Add a username!") #Виводжу попередження що ім'я не введене


def add_phone_to_user(args, User_book): #Функція додавання до користувача телефону ([name, phone], dict)
    n, p = args #Розбиваю список
    p = Address_Book.Phone(p).phone_validation() #Зберігаю завалідований номер телефону
    if p != None: #Роблю перевірку на відсутність валідації
        User_book.update_user_contacts(n, {"phone": p}) #Оновлюю телефон користувача


def add_birthday_to_user(args, User_book): #Функція додавання до користувача дня народження (['name', 'birthday'], dict)
    try:
        n, birthday = args #Пробую розбити список
        birthday = Address_Book.Birthday(birthday).birthday_validation() #Перезаписую ДН з валідацією
        User_book.update_user_contacts(n, {"birthday": birthday}) #Оновлюю ДН користувача в словнику
        
    except: print("Enter the command correctly \n-> add-birthday [name] [DD.MM.YYYY]") #Повертаю помилку


def add_email_to_user(args, User_book): #Функція додавання Email 
    try:
        n, email = args #Пробую розбити список
        email = Address_Book.Email(email).email_validation() #--------------------------------------------------
        User_book.update_user_contacts(n, {"email": email}) #Оновлюю почту користувача в словнику
        
    except: print("Enter the command correctly \n-> add-email [name] [Email]") #Повертаю помилку


def add_tag_to_user(args, User_book): #Функція додавання тегів до користувача
    nn, tg = args #Розбиваю список на змінні
    User_book.add_data_to_users(nn, "tag", tg) #Додаю тег до користувача


def searth_teg_user(args, User_book): #Функція пошуку користувача за тегом
    tn = "".join(args) #Додаю ім'я зі списку до рядка
    User_book.find_tags_users("tag", tn) #Шукаю тег








def add_notes(args, User_book): #Функція додавання нотаток до користувача з 
    try:
        u, com, nt = args #Пробую розбити список
        User_book.add_notes_to_users(u, [com, nt]) # [com, nt] #Оновлюю нотатки користувача в словнику
        
    except: print("Enter the command correctly \n-> note [name] [coment] [notes]") #Повертаю помилку


def view_note_user(namUser, User_book): #Функція для перегляду нотаток користувача
    try:
        dtUser = User_book.find_data_user("notes", namUser) #Шукаю в книзі нотатки користувача
        for du in dtUser: #Пробінаюсь циклом по словнику з нотатками
            print(du, "-", dtUser[du]) #Виводжу нотатки
    except: print(f"User {namUser} note is missing")


def remove_note_user(args, User_book): #Функція видалення однієї нотатки в користувача
    try:
        n, nd = args
        User_book.delete_data_users(n, "notes", nd) #
    except: print("Enter the command correctly \n-> remove-note [name] [coment]") #


def remove_user_notes_all(args, User_book): #Функція видалення всіх нотаток в користувача
    rnu = "".join(args) #Додаю ім'я зі списку до рядка
    User_book.delete_data_users(rnu, "notes", "all") #Видаляю нотатки користувача
 



""" Функції збереження і відкриття файлу .pkl"""
lincFile = "addressbook.pkl" #Посилання на файл (назва файлу)
def save_data(book, filename): #Функція збереження словника до файлу .pkl
    with open(filename, "wb") as f: #Відкриваю файл
        pickle.dump(book, f) #Створюю новий файл або переписую існуючий
        print("Book is saved")


def load_data(filename): #Функція зчитування файлу .pkl
    try: 
        with open(filename, "rb") as f: #Пробую відкрити файл
            try:
                print("Book has been updated")
                return pickle.load(f) #Декодую файл
            except: return Address_Book.AddressBook()
    except FileNotFoundError: #Якщо файл відсутній то створюю новий словник
        return Address_Book.AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

