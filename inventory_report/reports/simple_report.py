from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data):
        today = datetime.today().date()
        counts_by_name = Counter(
            d["nome_da_empresa"] for d in data
        ).most_common(1)
        lst_oldest_date = [d["data_de_fabricacao"] for d in data]
        lst_closest_date = [
            d["data_de_validade"] for d in data
            if datetime.strptime(d["data_de_validade"], "%Y-%m-%d").date()
            > today
        ]
        return f"""Data de fabricação mais antiga: {min(lst_oldest_date)}
Data de validade mais próxima: {min(lst_closest_date)}
Empresa com mais produtos: {counts_by_name[0][0]}"""
