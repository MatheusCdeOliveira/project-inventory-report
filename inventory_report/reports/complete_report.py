from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        counts_by_name = Counter(
            d["nome_da_empresa"] for d in data
        )
        report = ""
        for name, value in counts_by_name.items():
            report += f"- {name}: {value}\n"
        return (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{report}"
        )
