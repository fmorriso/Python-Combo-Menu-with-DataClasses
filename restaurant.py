from dataclasses import dataclass
from typing import ClassVar, Optional

from single_order import SingleOrder


@dataclass
class Restaurant:
    name: str
    orders: Optional[list[SingleOrder]] = None

    def add_order(self, order: SingleOrder):
        if self.orders is None:
            self.orders = []
        self.orders.append(order)

    def get_order_by_number(self, number: int) -> Optional[SingleOrder]:
        orders = [order for order in self.orders if order.number == number]
        if orders is None:
            return None
        if len(orders) == 1:
            return orders[0]
        return None

    def get_orders(self) -> list[SingleOrder]:
        return self.orders
