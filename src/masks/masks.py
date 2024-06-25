def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 4 и последние 4 цифры видимыми, а середину заменяя на звездочки.

    Параметры:
        card_number (str): Полный номер карты, который необходимо маскировать.

    Возвращает:
        str: Маскированный номер карты с пробелами для улучшения читаемости.
    """
    # Убедитесь, что номер карты не содержит пробелов перед маскированием
    card_number = card_number.replace(" ", "")
    # Маскировка номера карты с пробелами
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card_number


def get_mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя первые 2 и последние 2 цифры видимыми.

    Параметры:
        account_number (str): Полный номер счета, который необходимо маскировать.

    Возвращает:
        str: Маскированный номер счета, где середина номера заменена на звездочки для конфиденциальности.
    """
    masked_account_number = f"{account_number[:2]}****{account_number[-2:]}"
    return masked_account_number


# Пример использования функций
masked_card = get_mask_card_number("7000792289606361")
print(masked_card)  # Вывод: 700079******6361

masked_account = get_mask_account_number("73654108430135874305")
print(masked_account)  # Вывод: **4305
