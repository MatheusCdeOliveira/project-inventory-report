from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data):
        today = datetime.today().date()
        counts_by_name = Counter(
            d["nome_da_empresa"] for d in data
        ).most_common(1)[0][0]
        lst_oldest_date = []
        lst_closest_date = []
        for obj in data:
            d = datetime.strptime(obj["data_de_fabricacao"], "%Y-%m-%d").date()
            v = datetime.strptime(obj["data_de_validade"], "%Y-%m-%d").date()
            lst_oldest_date.append(d)
            if v > today:
                lst_closest_date.append(obj["data_de_validade"])
        return f"""Data de fabricação mais antiga: {min(lst_oldest_date)}
Data de validade mais próxima: {min(lst_closest_date)}
Empresa com mais produtos: {counts_by_name}"""
