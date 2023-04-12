import pytest

from src.math import Math


def test_plus_2_numbers():
    # Arrange
    x = 50
    y = 5

    # Act
    result = Math.plus(x, y)

    # Assert
    expected = 55
    assert expected == result


def test_minus_2_numbers():
    # Arrange
    x = 50
    y = 5

    # Act
    result = Math.minus(x, y)

    # Assert
    expected = 45
    assert expected == result


def test_multiplication_2_numbers():
    # Arrange
    x = 50
    y = 5

    # Act
    result = Math.multiplication(x, y)

    # Assert
    expected = 250
    assert expected == result


def test_divide_2_numbers():
    # Arrange
    x = 50
    y = 5

    # Act
    result = Math.divide(x, y)

    # Assert
    expected = 10
    assert expected == result
