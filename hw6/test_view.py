# перед запуском переименовать в test_view
# python -m pytest test_view.py -v
# coverage run -m pytest test_view.py -v
# coverage report

from io import StringIO
import pytest
from view import View

@pytest.fixture
def view():
    return View()

def test_out_text(view, capsys):
    view.out_text('Тест')
    captured = capsys.readouterr()
    assert captured.out == "Тест\n"

def test_input_text(view, monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('Тест'))
    res = view.input_text()
    assert res == 'Тест'

def test_print_menu(view, capsys):
    text_menu = "Выберите пункт меню цифрой: \n" \
            "1 - ввести первый массив, 2 - ввести второй массив,\n" \
            "3 - распечатать модель, 4 - сравнить массивы модели, 0 - выход"
    view.print_menu()
    captured = capsys.readouterr()
    assert captured.out == f"{text_menu}\n"

def test_menu(view, monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('3'))
    res = view.menu()
    assert res == 3

def test_input_array(view, monkeypatch):
    view = View()
    monkeypatch.setattr('sys.stdin', StringIO('1,2,3'))
    res = view.input_array()
    assert res == [1, 2, 3]


if __name__ == '__main__':
    pytest.main(['-v'])