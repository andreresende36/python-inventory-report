from typing import Optional

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        if not data:
            self._data = []
        else:
            self._data = data

    def add_data(self, data: list[Product]) -> None:
        if not self._data:
            self._data = data
        else:
            self._data += data

    @property
    def data(self) -> Optional[list[Product]]:
        return self._data
