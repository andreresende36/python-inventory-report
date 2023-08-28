from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    products: list[Product] = []
    for file in file_paths:
        if file.endswith(".json"):
            json_file = JsonImporter(file)
            data = json_file.import_data()
            products += data

        if file.endswith(".csv"):
            csv_file = CsvImporter(file)
            data = csv_file.import_data()
            products += data
    total_inventory = Inventory(products)
    return generate_report(total_inventory, report_type)


# def handle_inventory_addition(
#     companies_inventories: dict[str, int], inventory: Inventory
# ) -> dict[str, int]:
#     products = inventory.data
#     if products is not None:
#         for product in products:
#             if product.company_name not in companies_inventories:
#                 companies_inventories[product.company_name] = 1
#             else:
#                 companies_inventories[product.company_name] += 1
#     return companies_inventories


def generate_report(inventory: Inventory, report_type: str) -> str:
    if report_type == "simple":
        simple = SimpleReport()
        simple.add_inventory(inventory)
        return simple.generate()
    elif report_type == "complete":
        complete = CompleteReport()
        complete.add_inventory(inventory)
        return complete.generate()
    raise ValueError("Report type is invalid.")
