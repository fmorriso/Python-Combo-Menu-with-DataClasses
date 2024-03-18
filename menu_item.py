from dataclasses import dataclass
from typing import Optional


@dataclass
class MenuItem:
    category: str
    name: str
    price: float
    quantity: Optional[int] = 1
