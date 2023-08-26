from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        simple_report = super().generate()
        complete_report = "Stocked products by company:\n"
        for company, value in self.companies_inventories.items():
            complete_report += f"- {company}: {value}\n"
        return simple_report + complete_report
