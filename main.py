import sys
from importlib.metadata import version

from input_utilities import InputUtils
from restaurant import Restaurant
from single_order import SingleOrder


def get_order() -> SingleOrder:
    """creates a new order and returns the instance to the caller"""
    new_order = SingleOrder()

    new_order.get_sandwich()
    new_order.get_beverage()
    new_order.get_fries()
    new_order.get_ketchup_packets()
    new_order.check_for_discount()
    new_order.display()

    return new_order


def get_python_version() -> str:
    """returns the current version of python that is running the current program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


if __name__ == '__main__':
    print(f'Combo Menu using Data Classes using python version {get_python_version()}')
    print(f'Pyqt6 version: {get_package_version("pyqt6")}')
#    print(f'dataclasses version: {get_package_version("dataclasses")}')

    restaurant = Restaurant("Fred's Fast Food")
    print(f'Welcome to {restaurant.name} where the food and drinks are always delicious.')
    title: str = 'Another order?'
    question: str = 'Do you want to make another order?'
    while True:
        current_order: SingleOrder = get_order()
        restaurant.add_order(current_order)
        if not InputUtils.get_yesno_response(question, title):
            break

    title = 'Review orders?'
    question = 'Do you want to review your orders?'
    if InputUtils.get_yesno_response(question, title):
        for order in restaurant.get_orders():
            order.display()

    print(f'Thanks for visiting {restaurant.name}.  We appreciate your business.')
