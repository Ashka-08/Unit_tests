from BookRepository import BookRepository


class BookService:
    
    def __init__(self, bookRepository: BookRepository) -> None:
        self.__bookRepository = bookRepository

    @property
    def bookRepository(self) -> list:
        return self.__bookRepository
    
    @bookRepository.setter
    def bookRepository(self, bookRepository: BookRepository) -> None:
        self.__bookRepository = bookRepository

    def getAllBooks(self) -> list:
        return self.__bookRepository.allBooks