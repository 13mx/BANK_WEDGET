# Модуль generators

def filter_by_currency(transaction_list, currency_code):
    """
    Генератор, который принимает список словарей с банковскими операциями
    и возвращает итератор, выдающий операции в указанной валюте.
    """
    for transaction in transaction_list:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transaction_list):
    """
    Генератор, который принимает список словарей и возвращает описание
    каждой операции по очереди.
    """
    for transaction in transaction_list:
        yield transaction['description']


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт, который генерирует номера карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра.
    """
    for number in range(start, end + 1):
        yield f"{number:0>16}"


# Пример списка словарей, для которых должны работать функции модуля generators
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    # ... остальные транзакции ...
]

# Пример использования функций модуля generators
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    try:
        print(next(usd_transactions)["id"])
    except StopIteration:
        print("Нет транзакций в USD.")

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        break

for card_number in card_number_generator(1, 5):
    print(card_number)
