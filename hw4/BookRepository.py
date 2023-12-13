class BookRepository:
   
    def __init__(self, books: list) -> None:
        self.__books = books
   
    @property
    def allBooks(self) -> list:
        return self.__books
    
    @allBooks.setter
    def allBooks(self, books: list) -> None:
        self.__books = books
    
