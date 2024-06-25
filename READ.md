# Проект Управления Банковскими Транзакциями

## Описание

Этот проект предоставляет инструменты для фильтрации и сортировки банковских транзакций. Функции `filter_by_state` и `sort_by_date` позволяют пользователям организовывать транзакции по состоянию и дате соответственно.

## Функции

- `filter_by_state(transaction_list, state='EXECUTED')`: Фильтрует транзакции по заданному состоянию.
- `sort_by_date(transaction_list, descending=True)`: Сортирует транзакции по дате.
- `mask_account_card(account_number, mask_char='*', unmasked_digits=4)`: Скрывает номера банковских карт, оставляя видимыми последние четыре цифры.

## Недавние Обновления

- Разработана функция `mask_account_card` для маскировки номеров банковских карт.
- Добавлены тесты с использованием библиотеки `pytest` для проверки корректности маскировки.
- Исправлены ошибки формата входных данных для функции `mask_account_card`.
- Использованы регулярные выражения для улучшения гибкости обработки строк в функции `mask_account_card`.
- Исправлены ошибки `E902 FileNotFoundError` и `E302`, возникающие при использовании линтера Flake8.

## Использование

```python
# Фильтрация по состоянию 'EXECUTED'
executed_transactions = filter_by_state(transactions)

# Фильтрация по состоянию 'CANCELED'
canceled_transactions = filter_by_state(transactions, 'CANCELED')

# Сортировка по дате по убыванию
sorted_transactions_desc = sort_by_date(transactions)

# Сортировка по дате по возрастанию
sorted_transactions_asc = sort_by_date(transactions, False)

# Маскировка номера банковской карты
masked_card = mask_account_card('1234567890123456')
