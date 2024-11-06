all_commands = \
'''
Команди для контактів:
 1 - "hello" -> Привітання з користувачем
 2 - "add [ім'я]" -> Створюю користувача
 3 - "add-phone [ім'я] [номер телефону]" -> Зберігає список номерів телефону, ???при додаванні робить перевірку чи номер існує.
 4 - "phone [ім'я]" -> Виводить номер телефону контакту
 5 - "all" -> Виводить всі контакти з словниками
 6 - "close" -> Закриває програму із збереженням даних
 7 - "add-birthday [ім'я] [дата народження]" -> Додаю до контакту день народження
 8 - "show-birthday [ім'я]" -> Показую день народження контакту
 9??? - "birthdays" -> Повертає список користувачів, яких потрібно привітати на задану кількість днів від введеної дати
 10 - "open-book [link to file]" -> Команда для відкриття файлу в ручну (якщо не вказати назву то поверне пустий словник)
 11 - "remove-user [ім'я]" -> Команда видалення користувача
 12 - "add-email [ім'я] [Email]" -> Команда додавання електронної пошти до користувача
 13 - "save" -> Команда зберігання словника в файл .pkl
 14 - "help" -> Виводить всі доступні команди 
 15 - "exit" -> Закриває програму без збереження даних

 16--- - "show-user [name]" -> Виводить дані користувача
 17--- - "add-addres [name]" -> Додає адресу до користувача
 18--- - "show-addres [name]" -> Виводить адресу до користувача

Команди для нотатків:
 1 - "n [name] [coment] [notes]" -> Додавання нотаток до користувача або редагую існуючі
 2 - "view-notes [name]" -> Виводить нотатки користувача
 3 - "view-all-notes" -> Виводить всі нотатки всіх користувачів
 4 - "remove-notes-all [name]" -> Видаляє всі нотати в користувача
 5 - "remove-note [name] [comment]" -> Видаляє конкретну нотатку користувача
 
Команди тегів:
 1 - "add-tag [name] [tag]" -> Додає тег до користувача
 2 - "tag-user [tag]" -> Шукає користувача за тегом
'''



import Address_Book #Імпортую свій файл з користувачами
import Basic_functions #Імпортую файл з функціями




""" Основний цикл з парсингом команд"""
def parse_input(user_input): #Функція для парсингу команд
    cmd, *args = user_input.split() #Розбиваю команду
    cmd = cmd.strip().lower() #Записую команду в окрему змінну
    return cmd, *args #Повертаю команду і аргументи


def main(): #Основна функція з циклом 
    book = Address_Book.AddressBook() #Екземпляр класу AddressBook
    
    book.add_record(Basic_functions.load_data(Basic_functions.lincFile)) #Записую до книги декодовані дані з файлу
    
    print("Welcome to the assistant bot!")
    while True: #Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ") #Запитую команду
        
        try: #Якщо є команда то виконую перевірки
            command, *args = parse_input(user_input) #Зберігаю результат парсингу в змінні
    
            match command: #Команди
                
                case "hello": #Привітання
                    print("Hello! \nHow can I help you?")
                
                case "help": print(all_commands) #Команда з привітанням
                    
                case "all": Basic_functions.all_book(book) #Команда виведення всх контактів з AddressBook з усіма даними
                    
                case "add": Basic_functions.add_user_book(args, book) #???????????Команда додавання користувача до AddressBook
                
                case "remove-user": #Команда видалення користувача з AddressBook
                    du = "".join(args)
                    book.delete(du)
                    
                
                case "add-phone": #Додаю телефон до користувача
                    Basic_functions.add_phone_to_user(args, book)
                case "phone": #Виводжу телефон користувача
                    un = "".join(args) #Додаю ім'я зі списку до рядка
                    book.find_contacts_user(un, "phone") #Шукаю телефон користувача в книзі
                    
                
                case "add-birthday": #Додаю день народження до користувача
                    Basic_functions.add_birthday_to_user(args, book)
                case "show-birthday": #Виводжу день народження користувача
                    ub = "".join(args) #Додаю ім'я зі списку до рядка
                    book.find_contacts_user(ub, "birthday") #Шукаю день народження користувача в книзі
                    
                case "birthdays": #Виводжу дні народження користувачів на найближчий тиждень
                    print("Dictionary with greetings for the week: ", book.find_birthday_users_for_week())
                
                
                case "add-email": #Додаю пошту до користувача
                    Basic_functions.add_email_to_user(args, book)
                case "show-email": #Виводжу почту користувача
                    uem = "".join(args) 
                    book.find_contacts_user(uem, "email")
                
                #Теги користувача
                case "add-tag": Basic_functions.add_tag_to_user(args, book)
                case "tag-user": Basic_functions.searth_teg_user(args, book)


            

                
                #Нотатки
                case "n": #Додаю нотатки до користувача
                    Basic_functions.add_notes(args, book)
                
                case "view-notes": #Перегляд всіх нотаток користувача
                    vnU = "".join(args) #Додаю ім'я зі списку до рядка
                    Basic_functions.view_note_user(vnU, book)
                case "view-all-notes":
                    book.find_data_user("notes") #Виведення всіх нотаток користувача

                case "remove-note": #Видаляє нотатку в користувача
                    Basic_functions.remove_note_user(args, book)
                case "remove-notes-all":
                    Basic_functions.remove_user_notes_all(args, book)
                

            


            # #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
                case "open-book": #Команда для відкриття книги в ручну
                    lb = "".join(args) #Додаю посилання на файл зі списку до рядка
                    book.add_record(Basic_functions.load_data(lb)) #Записую до книги AddressBook декодовані дані з файлу
                    
                
                case "save": Basic_functions.save_data(book, Basic_functions.lincFile) #Зберігаю в файл .pkl книгу з користувачами
                
                case "close": break #Команда для закриття книги НЕ зберігає словник
                
                case "exit": #Команда для закриття книги зберігає словник
                    Basic_functions.save_data(book, Basic_functions.lincFile) #Зберігаю в файл .pkl книгу з користувачами
                    print("Good bye!")
                    break  
                
                
                case _: #Якщо команда не роспізнана
                    print("Invalid command!!!")
            
        except: print("Incorrect command...") #Якщо команда відсутня
    



if __name__ == "__main__":
    main()