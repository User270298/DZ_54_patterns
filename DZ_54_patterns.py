from abc import ABC, abstractmethod
import logging




class IBook(ABC):
    @abstractmethod
    def __init__(self, name: str, author: str, genre: str, year: str):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Book:
    def __init__(self, name: str, author: str, genre: str, year: str):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def get_info(self):
        return f"{self.name} by {self.author}, {self.genre}, {self.year}"


class ILibrarian(ABC):
    @abstractmethod
    def __init__(self, name: str, exp: str):
        pass

    @abstractmethod
    def add_book(self, book: IBook):
        pass

    @abstractmethod
    def delete_book(self, book: IBook):
        pass


    @abstractmethod
    def save_file(self, file):
        pass

    @abstractmethod
    def read_file(self, file):
        pass


class Librarian(ILibrarian):
    def __init__(self, name_lib: str, exp: str):
        self.name_lib = name_lib
        self.exp = exp
        self.books = []

    def add_book(self, book: IBook):
        self.books.append(book)

    def delete_book(self, book: IBook):
        for i in self.books:
            dct=i.__dict__
            for j in dct:
                print(dct[j])
                if book==dct[j]:
                    del i.__dict__
                    return

    def save_file(self, file):
        with open(file, 'a') as f:
            f.writelines(f"{[i.__dict__ for i in self.books]}")

    def read_file(self, file):
        with open(file, 'r') as f:
            print(f.read())


class IReader(ABC):
    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod
    def search_book_name(self, lib: ILibrarian, name_book):
        pass

    @abstractmethod
    def search_book_author(self, lib: ILibrarian, author):
        pass

    @abstractmethod
    def search_book_junge(self, lib: ILibrarian, junge):
        pass


class Reader(IReader):
    def __init__(self, name_reader: str):
        self.name_reader = name_reader

    def search_book_name(self, lib: ILibrarian, name_book):
        for i in librarian.books:
            dct = i.__dict__
            for j in dct:
                print(dct[j])
                if name_book == dct[j]:
                    print(i.__dict__)
                    return
        return 0

    def search_book_author(self, lib: ILibrarian, author):
        for i in librarian.books:
            dct = i.__dict__
            for j in dct:
                print(dct[j])
                if author == dct[j]:
                    print(i.__dict__)
                    return
        return 0

    def search_book_junge(self, lib: ILibrarian, junge):
        for i in librarian.books:
            dct = i.__dict__
            for j in dct:
                print(dct[j])
                if junge == dct[j]:
                    print(i.__dict__)
                    return
        return 0
def inputs():
    return input('Input next buttons:\n'
                '1- Add book \n'
                '2- Delete book\n'
                '3- Save to file\n'
                '4- Read file\n'
                '5-Reader move\n'
                '0- exit\n')


librarian = Librarian("John", 5)
reader=Reader('Mark')
def main():
    inp = inputs()

    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    while True:
        if inp == '0':
            break
        if inp == '1':
            book=Book(input('Input name:\n'),
                    input("Author\n"), input("Genre\n"), input("Year\n"))
            librarian.add_book(book)
            for i in librarian.books:
                print(i.__dict__)
            logging.info(f'{librarian.name_lib} add {book.__dict__}')
        elif inp == '2':
            name_book=input('Name book\n')
            librarian.delete_book(name_book)
            logging.info(f'{librarian.name_lib} delete {name_book}')
            for i in librarian.books:
                print(i.__dict__)
        elif inp == '3':
            librarian.save_file('new_file.txt')
            logging.info(f'{librarian.name_lib} save new_file.txt')
        elif inp == '4':
            librarian.read_file('new_file.txt')
            logging.info(f'{librarian.name_lib} read new_file.txt')
        elif inp=='5':
            vvod=input('Input\n'
                       '1- search name\n'
                       '2-search author\n'
                       '3-search junge\n')
            if vvod=='1':
                name=input('Input name\n')
                reader.search_book_name(librarian, name)
                logging.info(f'{reader.name_reader} search to the name  {name}')
            elif vvod=='2':
                author=input('Input author\n')
                reader.search_book_author(librarian, author)
                logging.info(f'{reader.name_reader} search to the name  {author}')
            elif vvod=='3':
                junge=input('Input junge\n')
                reader.search_book_junge(librarian, junge)
                logging.info(f'{reader.name_reader} search to the name  {junge}')

            else:
                continue

        inp = inputs()

if __name__ == '__main__':
    main()

