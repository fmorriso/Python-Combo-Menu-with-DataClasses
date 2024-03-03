import sys

from single_order import SingleOrder


def get_order() -> SingleOrder:
    order = SingleOrder()
    order.get_sandwich()
    order.get_beverage()
    order.get_fries()
    order.get_ketchup_packets()
    order.display()
    return order


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Combo Menu using Data Classes using python version {get_python_version()}')

    # TODO: surround get_order() with a loop that allows multiple orders to be taken and remembered.
    # one possibility is a Customer class with a list of orders of type SingleOrder
    current_order: SingleOrder = get_order()
