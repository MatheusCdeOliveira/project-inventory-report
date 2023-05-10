import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            root = ET.parse(path).getroot()
            data = []
            for item in root:
                d = {}
                for x in item:
                    d[x.tag] = x.text
                data.append(d)
            return data
        else:
            raise ValueError("Arquivo inválido")
