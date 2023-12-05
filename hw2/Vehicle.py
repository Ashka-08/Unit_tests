# Базовый класс ""Vehicle"" содержит абстрактные методы 
# ""testDrive()"" и ""park()"", а также поля 
# ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".

from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, 
        company: str, 
        model: str, 
        yearRelease: int, 
        numWhels: int, 
        speed: int) -> None:
        self.__company = company
        self.__model = model
        self.__yearRelease = yearRelease
        self.__numWheels = numWhels
        self.__speed = speed
    
    @abstractmethod
    def testDrive() -> None:
        pass

    @abstractmethod
    def park() -> None:
        pass

    @property
    def company(self) -> str:
        return self.__company
    
    @company.setter
    def company(self, company: str):
        self.__company = company

    @property
    def model(self) -> str:
        return self.__model
    
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def yearRelease(self) -> int:
        return self.__yearRelease
    
    @yearRelease.setter
    def yearRelease(self, yearRelease: int):
        self.__yearRelease = yearRelease

    @property
    def numWheels(self) -> int:
        return self.__numWheels
    
    @numWheels.setter
    def numWheels(self, numWheels: int):
        self.__numWheels = numWheels

    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed