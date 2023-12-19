# перед запуском переименовать в test_model
# python -m pytest test_model.py -v
# coverage run -m pytest test_model.py -v
# coverage report

import pytest
from model import Model

@pytest.fixture
def model():
    return Model()

def test_get_arr1():
    model = Model([1,2,3], [4,5,6])
    assert model.arr1 == [1, 2, 3]

def test_get_arr2():
    model = Model([1,2,3], [4,5,6])
    assert model.arr2 == [4, 5, 6]

def test_create_empty_model():
    assert str(Model()) == "Model([], []])"

def test_create_model():
    assert str(Model([1,2,3], [4,5,6])) == "Model([1, 2, 3], [4, 5, 6]])"

def test_add_arr1(model):
    model.arr1 = [4,5,6]
    assert model.arr1 == [4,5,6]

def test_add_arr2(model):
    model.arr2 = [4,5,6]
    assert model.arr2 == [4,5,6]

def test_get_averages():
    model = Model([1,2,3], [4,5,6])
    assert model.get_averages() == (2, 5)

def test_get_averages_exception():
    with pytest.raises(ValueError, match=r'Arrays must not be empty'):
        model = Model()
        model.get_averages()

def test_compare_averages_big_first():
    model = Model([4,5,6], [1,2,3])
    result = model.compare_averages()
    assert result == "Первый список имеет большее среднее значение"

def test_compare_averages_big_second():
    model = Model([1,2,3], [4,5,6])
    result = model.compare_averages()
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_equals():
    model = Model([1,2,3], [1,2,3])
    result = model.compare_averages()
    assert result == "Средние значения равны"


if __name__ == '__main__':
    pytest.main(['-v'])