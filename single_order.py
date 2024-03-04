from dataclasses import dataclass
from typing import ClassVar, Optional

from menu_item import MenuItem
from menu import Menu
from prompt_utility import PromptUtility
from datetime import datetime


# NOTE: we make almost every attribute optional so we can perform the
#       python equivalent of java's default constructor:
#       order = SingleOrder()
#       which has the added benefit of not having the world's largest constructor signature.

@dataclass
class SingleOrder:
    menu: ClassVar[Menu] = Menu()
    next_order_number: ClassVar[int] = 100

    order_number: Optional[int] = 0
    order_date_time: Optional[datetime] = None

    sandwich_type: Optional[str] = 'None'
    sandwich_cost: Optional[float] = 0.0

    beverage_size: Optional[str] = 'None'
    beverage_cost: Optional[float] = 0.0

    fries_size: Optional[str] = 'None'
    fries_cost: Optional[float] = 0.0

    ketchup_packets_quantity: Optional[int] = 0
    ketchup_packets_cost: Optional[float] = 0.0

    combo_discount_applied: Optional[bool] = False

    @property
    def total_cost(self):
        total: float = self.sandwich_cost + self.beverage_cost + self.fries_cost + self.ketchup_packets_cost
        if self.combo_discount_applied:
            total += Menu.COMBO_DISCOUNT_AMOUNT  # this is declared as a negative amount so we can display it easier
        return total

    def __init__(self):
        """augment the built-in DataClass constructor with some special stuff"""
        self.order_number = SingleOrder.get_next_order_number()
        self.order_date_time = datetime.now()

    @staticmethod
    def get_next_order_number() -> int:
        SingleOrder.next_order_number += 1
        return SingleOrder.next_order_number

    def get_sandwich(self) -> None:
        if not PromptUtility.get_yes_no_answer("Would you like a sandwich?>"):
            return

        # filter the menu for just sandwich choices
        available_choices: list[MenuItem] = Menu.get_menu_choices_for_category(category='Sandwich')

        # create prompt with choices and prices
        prompt = self.get_prompt_for_category("Which sandwich would you like to order: (", available_choices)

        while True:
            choice = input(prompt)
            if choice is None or len(choice) == 0:
                choice = "unknown"
            abbrev = choice[:1].lower()

            selection = None
            for available_choice in available_choices:
                if available_choice.name[:1].lower() == abbrev:
                    selection = available_choice
                    break

            if selection is None:
                print(f'{abbrev} is not a valid choice')
            else:
                print(f'{selection.name} is a great choice')
                break

        self.sandwich_type = selection.name
        self.sandwich_cost = selection.price

    def get_beverage(self) -> None:
        if not PromptUtility.get_yes_no_answer("Would you like a beverage?>"):
            return

        # filter the menu for just beverage choices
        available_choices: list[MenuItem] = Menu.get_menu_choices_for_category('Beverage')

        # create prompt with choices and prices
        prompt = self.get_prompt_for_category("What size beverage would you like to order: (", available_choices)

        while True:
            choice = input(prompt)
            if choice is None or len(choice) == 0:
                choice = "unknown"
            abbrev = choice[:1].lower()

            selection = None
            for available_choice in available_choices:
                if available_choice.name[:1].lower() == abbrev:
                    selection = available_choice
                    break

            if selection is None:
                print(f'{abbrev} is not a valid choice')
            else:
                print(f'{selection.name} is a great choice')
                break

        self.beverage_size = selection.name
        self.beverage_cost = selection.price

    def get_fries(self) -> None:
        if not PromptUtility.get_yes_no_answer("Would you like fries?>"):
            return

        # filter the menu for just french fries choices
        available_choices = Menu.get_menu_choices_for_category('Fries')

        # create the prompt with choices and prices
        prompt = self.get_prompt_for_category("What size french fries would you like to order: (", available_choices)

        # print(f'DEBUG: {prompt=}')
        while True:
            choice = input(prompt)
            if choice is None or len(choice) == 0:
                choice = "unknown"
            abbrev = choice[:1].lower()

            selection = None
            for available_choice in available_choices:
                if available_choice.name[:1].lower() == abbrev:
                    selection = available_choice
                    break

            if selection is None:
                print(f'{abbrev} is not a valid choice')
            else:
                print(f'{selection.name} is a great choice')
                break

        # Ask customer of they want to super-size their fries from Small to Large
        if selection.name[:1].lower() == 's':
            if PromptUtility.get_yes_no_answer('Do you want to super-size to a large?>'):
                abbrev = 'l'
                for available_choice in available_choices:
                    if available_choice.name[:1].lower() == abbrev:
                        selection = available_choice

        self.fries_size = selection.name
        self.fries_cost = selection.price

    def get_ketchup_packets(self):
        if not PromptUtility.get_yes_no_answer("Would you like any ketchup packets?>"):
            return

        per_each_cost: float = Menu.KETCHUP_PACKETS_PRICE_EACH
        n: int = PromptUtility.get_quantity(f"How many ketchup packets would you like at ${per_each_cost:.2f} each", 1,
                                            10)

        self.ketchup_packets_quantity = n
        self.ketchup_packets_cost = n * per_each_cost

    def check_for_discount(self):
        # don't give the discount more than once
        if self.combo_discount_applied:
            return
        if self.sandwich_cost > 0 and self.beverage_cost > 0 and self.fries_cost > 0:
            self.combo_discount_applied = True

    def get_prompt_for_category(self, leadin: str, available_choices: list[MenuItem]) -> str:
        prompt = leadin
        for available_choice in available_choices:
            prompt += f'{available_choice.name}: ${available_choice.price:.2f}, '
        prompt = prompt.removesuffix(', ')
        prompt += ") ?>"
        return prompt

    def display(self):
        if self.total_cost == 0:
            print('There are no selections in this order yet.')
            return
        # f"Date: {date:%m/%d/%Y}"
        print(
            f'Order number {self.order_number} placed on {self.order_date_time.date():%Y-%m-%d} at {self.order_date_time.time():%H:%M:%S}')

        output = f'\t{"Sandwich:":20}'
        if self.sandwich_cost > 0:
            output += f'{self.sandwich_type:10}${self.sandwich_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Beverage:":20}'
        if self.beverage_cost > 0:
            output += f'{self.beverage_size:10}${self.beverage_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Fries:":20}'
        if self.fries_cost > 0:
            output += f'{self.fries_size:10}${self.fries_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Ketchup packets: ":20}'
        if self.ketchup_packets_cost > 0:
            output += f'{self.ketchup_packets_quantity:<9} ${self.ketchup_packets_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        if self.combo_discount_applied:
            output = f'\t{"Combo discount":30}${Menu.COMBO_DISCOUNT_AMOUNT:5.2f}'
            print(output)

        print(f'{"Total:":34}${self.total_cost:5.2f}')
