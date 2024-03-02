from dataclasses import dataclass
from typing import ClassVar, Optional


# NOTE: we make every attribute optional so we can perform the
#       python equivalent of java's default constructor:
#       order = SingleOrder()
#       which has the added benefit of not having the world's largest constructor signature.

@dataclass
class SingleOrder:
    KETCHUP_PACKETS_PRICE_EACH: ClassVar[float] = 0.25
    COMBO_DISCOUNT_AMOUNT: ClassVar[float] = 1.0

    next_order_number: ClassVar[int] = 100

    order_number: Optional[int] = 0
    total_cost: Optional[float] = 0.0

    sandwich_type: Optional[str] = 'None'
    sandwich_cost: Optional[float] = 0.0

    beverage_size: Optional[str] = 'None'
    beverage_cost: Optional[float] = 0.0

    fries_size: Optional[str] = 'None'
    fries_cost: Optional[float] = 0.0

    ketchup_packets: Optional[int] = 0
    ketchup_packets_cost: Optional[float] = 0.0

    combbo_discount_applied: Optional[bool] = False

    def __init__(self):
        """augment the built-in DataClass constructor with some special stuff"""
        self.order_number = SingleOrder.get_next_order_number()

    @staticmethod
    def get_next_order_number() -> int:
        SingleOrder.next_order_number += 1
        return SingleOrder.next_order_number

    def display_order(self):
        print(f'Your Order:')
        print(f'\tSandwich: {self.sandwich_type:20}${self.sandwich_cost:5.2f}')

