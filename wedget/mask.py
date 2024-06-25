def mask_account_card(info):
    parts = info.split()
    # Определяем, является ли информация картой или счетом
    if "Счет" in info:
        # Маскировка для счета
        return f"{parts[0]} **{parts[1][-4:]}"
    else:
        # Маскировка для карты
        return f"{parts[0]} {parts[1]} {parts[2][:2]}** **** {parts[3]}"


# Пример использования
print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

