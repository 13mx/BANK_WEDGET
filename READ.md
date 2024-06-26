# Проект Управления Банковскими Транзакциями

## Описание

Этот проект предоставляет инструменты для фильтрации и сортировки банковских транзакций, а также генераторы для упрощения работы с транзакциями и повышения безопасности данных.

## Функции

- `filter_by_state(transaction_list, state='EXECUTED')`: Фильтрует транзакции по заданному состоянию.
- `sort_by_date(transaction_list, descending=True)`: Сортирует транзакции по дате.
- `filter_by_currency(transaction_list, currency_code)`: Фильтрует транзакции по валютному коду.
- `transaction_descriptions(transaction_list)`: Возвращает описания транзакций.
- `card_number_generator(start, end)`: Генерирует защищённые номера банковских карт.

## Использование

```python
# Примеры фильтрации и сортировки
executed_transactions = filter_by_state(transaction_list, 'EXECUTED')
canceled_transactions = filter_by_state(transaction_list, 'CANCELED')
sorted_transactions_desc = sort_by_date(transaction_list)
sorted_transactions_asc = sort_by_date(transaction_list, False)

# Примеры использования генераторов
usd_transactions = filter_by_currency(transaction_list, "USD")
descriptions = transaction_descriptions(transaction_list)
for card_number in card_number_generator(1, 5):
    print(card_number)
