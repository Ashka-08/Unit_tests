# $ python -m unittest Vehicle_unittest.py -v

import unittest
from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Dodge', 'Ram', 2010)
        self.motorcycle = Motorcycle('Yamaha', 'YZF-R3', 2020)

    def test_car_is_instance_of_vehicle(self):
        """Проверить, что экземпляр объекта Car также является экземпляром 
        транспортного средства (используя оператор instanceof).
        """
        self.assertIsInstance(self.car, Vehicle)


    def test_car_numWheels(self):
        """Проверить, что объект Car создается с 4-мя колесами.
        """
        self.assertEqual(self.car.numWheels, 4)

    def test_motorcycle_numWheels(self):
        """Проверить, что объект Motorcycle создается с 2-мя колесами.
        """
        self.assertEqual(self.motorcycle.numWheels, 2)

    def test_car_testDrive(self):
        """Проверить, что объект Car развивает скорость 60 в режиме 
        тестового вождения (используя метод testDrive()).
        """
        self.car.testDrive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed(self):
        """Проверить, что объект Motorcycle развивает скорость 75 в режиме 
        тестового вождения (используя метод testDrive()).
        """
        self.motorcycle.testDrive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park(self):
        """Проверить, что в режиме парковки (сначала testDrive, потом park, 
        т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
        """
        self.car.testDrive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park(self):
        """Проверить, что в режиме парковки (сначала testDrive, потом park, 
        т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
        """
        self.motorcycle.testDrive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)