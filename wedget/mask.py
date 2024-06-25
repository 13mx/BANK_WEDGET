import re


def mask_account_card(info):
    # Регулярное выражение для карты Visa и счета
    visa_pattern = re.compile(r'Visa (\w+ )*(\d{4}) (\d{4}) (\d{4}) (\d{4})')
    account_pattern = re.compile(r'Счет (\d+)')

    visa_match = visa_pattern.search(info)
    account_match = account_pattern.search(info)

    if visa_match:
        additional_words = visa_match.group(1) if visa_match.group(1) else ''
        return f"Visa {additional_words}{visa_match.group(2)} {visa_match.group(3)[:2]}** **** {visa_match.group(5)}"
    elif account_match:
        account_number = account_match.group(1)
        return f"Счет **{account_number[-4:]}"
    else:
        raise ValueError("Invalid input format")

# Теперь функция может корректно обрабатывать и маскировать как номера карт V
