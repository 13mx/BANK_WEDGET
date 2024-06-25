import pytest
from src.masks.masks import get_mask_card_number, get_mask_account_number


# Тесты для функции get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 **** **** 6361"),
    ("1234567812345678", "1234 **** **** 5678")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тесты для функции get_mask_account_number
@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "73****4305"),
    ("12345678901234567890", "12****7890")
])
def test_get_mask_account_number(account_number, expected):
    assert get_mask_account_number(account_number) == expected
