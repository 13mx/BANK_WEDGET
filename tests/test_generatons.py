from generators.generatons import filter_by_currency, transaction_descriptions, card_number_generator

# Тестовые данные
transactions_test_data = [
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
    # ... другие транзакции ...
]


def test_filter_by_currency():
    # Проверка фильтрации по валюте USD
    usd_transactions = list(filter_by_currency(transactions_test_data, "USD"))
    assert all(tx['operationAmount']['currency']['code'] == "USD" for tx in usd_transactions)


def test_transaction_descriptions():
    # Проверка получения описаний транзакций
    descriptions = list(transaction_descriptions(transactions_test_data))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        # ... ожидаемые описания других транзакций ...
    ]


def test_card_number_generator():
    # Проверка генератора номеров карт
    card_numbers = list(card_number_generator(1, 5))
    assert card_numbers == [
        "0000000000000001",
        "0000000000000002",
        "0000000000000003",
        "0000000000000004",
        "0000000000000005"
    ]

# Для запуска тестов используйте команду: pytest -v
