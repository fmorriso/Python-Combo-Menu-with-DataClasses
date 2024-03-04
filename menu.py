from dataclasses import dataclass
from typing import ClassVar

from menu_item import MenuItem


@dataclass
class Menu:
    choices: ClassVar[list[MenuItem]] = []

    KETCHUP_PACKETS_PRICE_EACH: ClassVar[float] = 0.25
    COMBO_DISCOUNT_AMOUNT: ClassVar[float] = -1.0

    def __init__(self) -> None:
        if Menu.choices is None or len(Menu.choices) == 0:
            Menu.build()

    @staticmethod
    def build():
        """build menu that is the same for all orders"""
        category = 'Sandwich'
        for selection in (['Chicken', 5.25], ['Beef', 6.25], ['Tofu', 5.75]):
            menu_item = MenuItem(category, selection[0], selection[1])
            Menu.choices.append(menu_item)

        category = 'Beverage'
        for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
            menu_item = MenuItem(category, selection[0], selection[1])
            Menu.choices.append(menu_item)

        category = 'Fries'
        for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
            menu_item = MenuItem(category, selection[0], selection[1])
            Menu.choices.append(menu_item)

    @staticmethod
    def add_menu_item(item: MenuItem) -> None:
        Menu.choices.append(item)

    @staticmethod
    def get_menu_choices_for_category(category: str) -> list[MenuItem]:
        # filter the menu for just the specified category choices
        available_choices: list[MenuItem] = [item for item in Menu.choices if item.category == category]
        return available_choices
