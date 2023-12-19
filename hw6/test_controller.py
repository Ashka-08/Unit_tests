# перед запуском переименовать в test_controller
# python -m pytest test_controller.py -v
# coverage run -m pytest test_controller.py -v
# coverage report

from io import StringIO
from unittest.mock import MagicMock, Mock
import pytest
from controller import Controller
from view import View
from model import Model


def test_create():
    controller = Controller()
    assert str(controller.model) == "Model([], []])"

def test_create_with_params_integrate():
    model = Model([1,3], [2,4])
    controller = Controller(model=model)

    assert str(controller.model) == "Model([1, 3], [2, 4]])"

def test_menu(capsys):
    controller = Controller()
    text_menu = "Выберите пункт меню цифрой: \n" \
            "1 - ввести первый массив, 2 - ввести второй массив,\n" \
            "3 - распечатать модель, 4 - сравнить массивы модели, 0 - выход"

    controller.view.print_menu()
    captured = capsys.readouterr()

    assert captured.out == f"{text_menu}\n"

def test_arr2_bigger(capsys):
    model = Model([1,2,3], [4,5,6])
    controller = Controller(model=model)

    controller.view.out_text(controller.model.compare_averages())
    captured = capsys.readouterr()

    assert captured.out == "Второй список имеет большее среднее значение\n"

def test_arr1_bigger(capsys):
    controller = Controller()
    controller.model.arr1 = [8,9,10]
    controller.model.arr2 = [4,5,6]

    controller.view.out_text(controller.model.compare_averages())
    captured = capsys.readouterr()

    assert captured.out == "Первый список имеет большее среднее значение\n"


if __name__ == '__main__':
    pytest.main(['-v'])