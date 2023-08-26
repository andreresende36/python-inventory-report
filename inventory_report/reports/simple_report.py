from datetime import date, datetime

from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self._inventory_list: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventory_list.append(inventory)

    def generate(self) -> str:
        products = [
            product
            for inventory in self.inventory_list
            if inventory.data is not None
            for product in inventory.data
        ]

        oldest_manufacturing_date = date.today()
        closest_expiration_date = date(9999, 12, 31)
        companies_inventories: dict[str, int] = {}

        for product in products:
            manufacturing_date = datetime.strptime(
                product.manufacturing_date, "%Y-%m-%d"
            ).date()

            expiration_date = datetime.strptime(
                product.expiration_date, "%Y-%m-%d"
            ).date()

            company_name = product.company_name

            if manufacturing_date < oldest_manufacturing_date:
                oldest_manufacturing_date = manufacturing_date

            if (
                expiration_date > date.today()
                and expiration_date < closest_expiration_date
            ):
                closest_expiration_date = expiration_date

            if company_name not in companies_inventories:
                companies_inventories[company_name] = 1
            else:
                companies_inventories[company_name] += 1

        company_largest_inventory = max(
            companies_inventories,
            key=lambda company: companies_inventories[company],
        )

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: "
            f"{company_largest_inventory}\n"
        )

    @property
    def inventory_list(self) -> list[Inventory]:
        return self._inventory_list
