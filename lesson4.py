AVAILABLE_ITEMS = ["яблуко", "банан", "апельсин", "молоко", "хліб"]
PRICES = {"яблуко": 15.50, "банан": 30.00, "апельсин": 45.99, "молоко": 25.00, "хліб": 20.00, "масло": 50.00}

def format_price(price):
    return f"{price:.2f} грн"

def check_stock(*items):
    return {item: item in AVAILABLE_ITEMS for item in items}

def process_order():
    print(f"Сьогодні в наявності: {', '.join(AVAILABLE_ITEMS)}")

    user_input = input("Введіть товари, які хочете замовити, через кому: \n> ")
    ordered_items = [item.strip().lower() for item in user_input.split(',') if item.strip()]

    if not ordered_items:
        print("Ви нічого не обрали. Замовлення скасовано.")
        return

    stock_info = check_stock(*ordered_items)

    total_price = 0
    valid_items_with_prices = []

    for item in ordered_items:
        price = PRICES.get(item)
        if price is not None:
            total_price += price
            valid_items_with_prices.append((item, price))
        else:
            print(f"Увага: Товар '{item}' не знайдено в нашому асортименті.")

    if not valid_items_with_prices and any(item not in PRICES for item in ordered_items):
        print("Жоден з обраних товарів не знайдено в прайсі. Замовлення скасовано.")
        return

    print(f"Поточна сума: {format_price(total_price)}")
    action = input("Оберіть дію:\n[1] Купити\n[2] Просто переглянути ціну\n> ").strip()

    if action == '1':
        all_available = all(stock_info.get(item, False) for item in ordered_items)

        if all_available:
            print("\nЗамовлення успішно оформлено!")
            print(f"До сплати: {format_price(total_price)}")
        else:
            print("\nНеможливо оформити замовлення.")
            print("Наступні товари відсутні на складі або невідомі:")
            for item in ordered_items:
                if not stock_info.get(item):
                    print(f"- {item}")

    elif action == '2':
        print("\nЧек")
        for item, price in valid_items_with_prices:
            print(f"{item}: {format_price(price)}")

        print(f"Загальна сума: {format_price(total_price)}")

    else:
        print("Невірна опція. Будь ласка, оберіть [1] або [2].")


if __name__ == "__main__":
    process_order()