from dataclasses import dataclass
from typing import ClassVar, Optional

from menu_item import MenuItem


# NOTE: we make almost every attribute optional so we can perform the
#       python equivalent of java's default constructor:
#       order = SingleOrder()
#       which has the added benefit of not having the world's largest constructor signature.

@dataclass
class SingleOrder:
    KETCHUP_PACKETS_PRICE_EACH: ClassVar[float] = 0.25
    COMBO_DISCOUNT_AMOUNT: ClassVar[float] = 1.0
    menu: ClassVar[list[MenuItem]] = []
    next_order_number: ClassVar[int] = 100

    order_number: Optional[int] = 0

    sandwich_type: Optional[str] = 'None'
    sandwich_cost: Optional[float] = 0.0

    beverage_size: Optional[str] = 'None'
    beverage_cost: Optional[float] = 0.0

    fries_size: Optional[str] = 'None'
    fries_cost: Optional[float] = 0.0

    ketchup_packets: Optional[int] = 0
    ketchup_packets_cost: Optional[float] = 0.0

    combo_discount_applied: Optional[bool] = False

    @property
    def total_cost(self):
        total: float = self.sandwich_cost + self.beverage_cost + self.fries_cost
        if self.combo_discount_applied:
            total -= SingleOrder.COMBO_DISCOUNT_AMOUNT * self
        return total

    def __init__(self):
        """augment the built-in DataClass constructor with some special stuff"""
        self.order_number = SingleOrder.get_next_order_number()
        if len(SingleOrder.menu) == 0:
            SingleOrder.build_menu()

    @staticmethod
    def build_menu():
        """build menu that is the same for all orders"""
        category = 'Sandwich'
        for selection in (['Chicken', 5.25], ['Beef', 6.25], ['Tofu', 5.75]):
            menu_item = MenuItem(category, selection[0], selection[1])
            SingleOrder.menu.append(menu_item)

        category = 'Beverage'
        for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
            menu_item = MenuItem(category, selection[0], selection[1])
            SingleOrder.menu.append(menu_item)

        category = 'Fries'
        for selection in (['Small', 1.0], ['Medium', 1.5], ['Large', 2.0]):
            menu_item = MenuItem(category, selection[0], selection[1])
            SingleOrder.menu.append(menu_item)

        category = 'Condiments'
        menu_item = MenuItem(category, 'Ketchup packets', 0.25, 0)
        SingleOrder.menu.append(menu_item)

    @staticmethod
    def get_next_order_number() -> int:
        SingleOrder.next_order_number += 1
        return SingleOrder.next_order_number

    def get_sandwich(self) -> None:
        if not SingleOrder.get_yes_no_answer("Would you like a sandwich?>"):
            return

        # filter the menu for just sandwich choices
        available_choices: list[MenuItem] = self.get_menu_choices_for_category('Sandwich')

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
        if not SingleOrder.get_yes_no_answer("Would you like a beverage?>"):
            return

        # filter the menu for just beverage choices
        available_choices: list[MenuItem] = self.get_menu_choices_for_category('Beverage')

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
        if not SingleOrder.get_yes_no_answer("Would you like fries?>"):
            return

        # filter the menu for just french fries choices
        available_choices = self.get_menu_choices_for_category('Fries')

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
            if SingleOrder.get_yes_no_answer('Do you want to super-size to a large?>'):
                abbrev = 'l'
                for available_choice in available_choices:
                    if available_choice.name[:1].lower() == abbrev:
                        selection = available_choice

        self.fries_size = selection.name
        self.fries_cost = selection.price

    def get_menu_choices_for_category(self, category: str) -> list[MenuItem]:
        # filter the menu for just the specified category choices
        filtered_items = filter(lambda item: item.category == category, SingleOrder.menu)
        available_choices = list(filtered_items)
        return available_choices

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

        print(f'Order number {self.order_number}')

        output = f'\t{"Sandwich:":15}'
        if self.sandwich_cost > 0:
            output += f'{self.sandwich_type:10}${self.sandwich_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Beverage:":15}'
        if self.beverage_cost > 0:
            output += f'{self.beverage_size:10}${self.beverage_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Fries:":15}'
        if self.fries_cost > 0:
            output += f'{self.fries_size:10}${self.fries_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        print(f'{"Total:":29}${self.total_cost:5.2f}')

    @staticmethod
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


if __name__ == '__main__':
    def display(self):
        if self.total_cost == 0:
            print('There are no selections in this order yet.')
            return

        print(f'Order number {self.order_number}')

        output = f'\t{"Sandwich:":15}'
        if self.sandwich_cost > 0:
            output += f'{self.sandwich_type:10}${self.sandwich_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Beverage:":15}'
        if self.beverage_cost > 0:
            output += f'{self.beverage_size:10}${self.beverage_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        output = f'\t{"Fries:":15}'
        if self.fries_cost > 0:
            output += f'{self.fries_size:10}${self.fries_cost:5.2f}'
        else:
            output += f'{"None":10}'
        print(output)

        print(f'{"Total:":29}${self.total_cost:5.2f}')


    @staticmethod
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


    @staticmethod
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
