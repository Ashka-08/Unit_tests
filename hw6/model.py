from statistics import mean


class Model:
    """Класс Модель
    Хранит параметры arr1 И arr2 в виде целочисленных массивов
    Умеет определять массив с наибольшим средним значением
    """
    def __init__(self, arr1=[], arr2=[]) -> None:
        self.__arr1 = arr1
        self.__arr2 = arr2
    
    @property
    def arr1(self) -> list[int]:
        return self.__arr1
    
    @arr1.setter
    def arr1(self, arr1: list[int]) -> None:
        self.__arr1 = arr1
    
    @property
    def arr2(self) -> list[int]:
        return self.__arr2
    
    @arr2.setter
    def arr2(self, arr2: list[int]) -> None:
        self.__arr2 = arr2

    def get_averages(self) -> tuple[int, int]:
        """Метод получения средних значений массивов.
        Возвращает кортеж.
        Бросает исключение ValueError"""
        if self.__arr1 and self.__arr2:
            return int(mean(self.__arr1)), int(mean(self.__arr2))
        else:
            raise ValueError("Arrays must not be empty")
    
    def compare_averages(self) -> str:
        """ Метод сравнения массива с наибольшим средним значением
        Возвращает строку
        """
        try:
            average1, average2 = self.get_averages()
        except ValueError as e:
            return e
        if average1 and average2:
            if average1 > average2:
                return "Первый список имеет большее среднее значение"
            elif average1 < average2:
                return "Второй список имеет большее среднее значение"
            else:
                return "Средние значения равны"
    
    def __repr__(self) -> str:
        return f"Model({self.__arr1}, {self.__arr2}])"

if __name__ == "__main__":
    m = Model()
    print(m) #Model([], []])
    print(m.compare_averages()) #Arrays must not be empty

    m.arr1=[1,2,3]
    m.arr2=[4,5,6]
    print(m) #Model([1, 2, 3], [4, 5, 6]])
    print(m.compare_averages()) #Второй список имеет большее среднее значение

    m.arr2=[1,2,3]
    print(m) #Model([1, 2, 3], [1, 2, 3]])
    print(m.compare_averages()) #Средние значения равны