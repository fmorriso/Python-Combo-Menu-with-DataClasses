import sys

from menu_item import MenuItem
from single_order import *

menu: list[MenuItem] = []
order = SingleOrder()


def build_menu():
    global menu

    category = 'Sandwich'
    for selection in (['Chicken', 5.25], ['Beef', 6.25], ['Tofu', 5.75]):
        menu_item = MenuItem(category, selection[0], selection[1])
        menu.append(menu_item)

    category = 'Beverage'
    for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
        menu_item = MenuItem(category, selection[0], selection[1])
        menu.append(menu_item)

    category = 'Fries'
    for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
        menu_item = MenuItem(category, selection[0], selection[1])
        menu.append(menu_item)

    category = 'Condiments'
    menu_item = MenuItem(category, 'Ketchup packets', 0.25, 0)
    menu.append(menu_item)


def new_order():
    global order
    order = SingleOrder()


def get_order():
    new_order()


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_yes_no_answer(question: str) -> bool:
    while True:
        answer = input(question)
        if answer is None or len(answer) == 0:
            print("please respond with y, n, Yes, yes, No or no")
        else:
            answer = answer.lower()[:1]
            match answer:
                case 'y':
                    return True

                case 'n':
                    return False

                case _:
                    print("please respond with y, n, Yes, yes, No or no")


def get_quantity(question: str, min_value: int = 0, max_value: int = 10) -> int:
    """Prompt for a number between min_value and max_value"""
    question = f'{question} (between {min_value} and {max_value})?>'
    count: int = min_value - 1
    while count < min_value or count > max_value:
        try:
            count = int(input(question))
            if count < min_value or count > max_value:
                print(f'Please enter a number between {min_value} and {max_value}.')
            else:
                return count
        except ValueError:
            print(f'Please enter a value between {min_value} and {max_value}')


def get_sandwich():
    filtered_items = filter(lambda item: item.category == 'Sandwich', menu)
    display_items = list(filtered_items)
    print(f'{display_items=}')


if __name__ == '__main__':
    print(f'Combo Menu using Data Classes using python version {get_python_version()}')

    build_menu()
    print(f'{menu=}')

    order = SingleOrder()
    order.order_number = SingleOrder.get_next_order_number()
    get_sandwich()
