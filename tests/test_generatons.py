from generators.generatons import filter_by_currency, transaction_descriptions, card_number_generator


# Тесты для функции filter_by_currency
def test_filter_by_currency():
    transactions = [
        {
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            }
        },
        {
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                }
            }
        }
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]['operationAmount']['currency']['code'] == "USD"


# Тесты для функции transaction_descriptions
def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"}
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации", "Покупка в магазине"]


# Тесты для функции card_number_generator
def test_card_number_generator():
    card_numbers = list(card_number_generator(1, 5))
    assert len(card_numbers) == 5
    for number in card_numbers:
        assert len(number) == 16
        assert number.startswith("XXXXXX")
