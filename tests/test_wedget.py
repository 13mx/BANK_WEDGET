import pytest
from wedget.mask import mask_account_card
from wedget.data import get_data

# Параметры для тестирования функции mask_account_card
account_card_params = [
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
    ("Неверный ввод", ValueError)
]

# Параметры для тестирования функции get_data
date_params = [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2018-07-11 02:26:18", ValueError),
    ("2020-02-29T00:00:00.000000", "29.02.2020"),
    ("2019-04-30T23:59:59.999999", "30.04.2019"),
    ("2023-01-01T00:00:00.000000", "01.01.2023")
]


# Тесты для функции mask_account_card с использованием параметризации
@pytest.mark.parametrize("test_input, expected", account_card_params)
def test_mask_account_card(test_input, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            mask_account_card(test_input)
    else:
        assert mask_account_card(test_input) == expected


# Тесты для функции get_data с использованием параметризации
@pytest.mark.parametrize("test_input, expected", date_params)
def test_get_data(test_input, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            get_data(test_input)
    else:
        assert get_data(test_input) == expected
