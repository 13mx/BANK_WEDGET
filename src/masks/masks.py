def get_mask_card_number(card_number: str) -> str:
    card_number = card_number.replace(" ", "")
    # Измененная маскировка номера карты
    masked_card_number = f"{card_number[:4]} **** **** {card_number[-4:]}"
    return masked_card_number


def get_mask_account_number(account_number: str) -> str:
    # Убедимся, что номер счета имеет достаточную длину
    if len(account_number) < 6:
        return account_number
    # Обновленная функция с фиксированным количеством звездочек
    return f"{account_number[:2]}****{account_number[-4:]}"


# Пример использования функций
masked_card = get_mask_card_number("7000792289606361")
print(masked_card)  # Вывод: 700079******6361

masked_account = get_mask_account_number("73654108430135874305")
print(masked_account)  # Вывод: **4305
