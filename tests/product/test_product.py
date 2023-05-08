from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(1, "i5 13600K", "Intel", "13/02/2023", "NA", 45, "No")
    assert product.id == 1
    assert product.nome_do_produto == "i5 13600K"
    assert product.nome_da_empresa == "Intel"
    assert product.data_de_fabricacao == "13/02/2023"
    assert product.data_de_validade == "NA"
    assert product.numero_de_serie == 45
    assert product.instrucoes_de_armazenamento == "No"
