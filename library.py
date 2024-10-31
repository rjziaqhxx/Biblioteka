class Book:
    def __init__(self, title, author, isbn, available):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = available

    def borrow(self):
        if self.__available == True:
            self.__available = False
            print('Ksiazka jest pozyczona')
        else:
            print('Ksiazki nie ma')

    def return_book(self):
        if self.__available == False:
            self.__available = True
            print('Ksiazke zwrocono')
        else:
            print('Blad')

    def is_available(self):
        if self.__available == True:
            print('Ksizka jest')
        else:
            print('Ksiazki nie ma')

    
    @classmethod
    def create_from_input(cls):
        title = input('Podaj tytul - ')
        author = input('Podaj autora - ')
        isbn = int(input('Podaj numer - '))
        available = bool(input('Czy jest? - '))

        return cls(title, author, isbn, available)



class Person:
    def __init__(self, name, id_number,):
        self.__name = name
        self.__id_number = id_number

    def get_info(self):
        print(f'Name: {self.__name}, ID number: {self.__id_number}')

    @classmethod
    def create_from_input(cls):
        name = input('Podaj imie i nazwisko - ')
        id_number = int(input('Podaj id - '))

        return cls(name, id_number)   



class Reader(Person):
    def __init__(self, name, id_number,):
        super().__init__(name, id_number)

    def borrow(self):
        a.borrow()

    def return_book(self):
        a.return_book()



class Librarian(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
    
    def check_available(self):
        a.is_available()


libr = Librarian('Anton', 2332)
read = Reader('Josh', 221)
a = Book('Kik', 'josh', 1212, True)

def menu():
    print('1. Borrow')
    print('2. Return')
    print('3. Is available')
    print('4. Wyjdz')
    user_input = int(input('Wybierz - '))
    
    if user_input == 1:
        read.borrow()
    elif user_input == 2:
        read.return_book()
    elif user_input == 3:
        libr.is_available()
    elif user_input == 4:
        exit()

while True:
    menu()
