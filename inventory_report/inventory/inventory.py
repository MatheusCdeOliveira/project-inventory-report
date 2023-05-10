from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def read_ext(path):
        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)
        if path.endswith(".json"):
            data = JsonImporter.import_data(path)
        if path.endswith(".xml"):
            data = XmlImporter.import_data(path)
        return data

    @staticmethod
    def import_data(path, string):
        data = Inventory.read_ext(path)

        if string == 'simples':
            return SimpleReport.generate(data)
        elif string == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError("Invalid value")
