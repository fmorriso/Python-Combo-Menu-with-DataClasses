from dataclasses import dataclass
from typing import ClassVar, Optional

@dataclass
class MenuItem:
    category: str
    name: str
    price: float
    quantity: Optional[int] = 1
