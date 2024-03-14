import sys

from prompt_utility import PromptUtility
from restaurant import Restaurant
from single_order import SingleOrder


def get_order() -> SingleOrder:
    order = SingleOrder()
    order.get_sandwich()
    order.get_beverage()
    order.get_fries()
    order.get_ketchup_packets()
    order.check_for_discount()
    order.display()

    return order


def get_python_version() -> str:
    """returns the current version of python that is running the current program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Combo Menu using Data Classes using python version {get_python_version()}')

    restaurant = Restaurant("Fred's Fast Food")
    print(f'Welcome to {restaurant.name} where the food and drinks are always delicious.')
    while True:
        current_order: SingleOrder = get_order()
        restaurant.add_order(current_order)
        if not PromptUtility.get_yes_no_answer('Do you want to make another order?>'):
            break

    if PromptUtility.get_yes_no_answer('Do you want to review your orders?>'):
        for order in restaurant.get_orders():
            order.display()

    print(f'Thanks for visiting {restaurant.name}.  We appreciate your business.')
