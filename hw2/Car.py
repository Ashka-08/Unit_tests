# Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. 
# При создании объекта ""Car"", число колес устанавливается в 4, а скорость в 0. 
# В методе ""testDrive()"" скорость устанавливается на 60, 
# а в методе ""park()"" - обратно в 0.

from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, 
        company: str, 
        model: str, 
        yearRelease: int) -> None:
        super().__init__(company, model, yearRelease, numWhels=4, speed=0)

    def testDrive(self) -> None:
        self._speed = 60

    def park(self) -> None:
        self._speed = 0
    
    def __str__(self) -> str:
        return f"This car is a {self.__yearRelease} year make {self.__company} model {self.__model}"