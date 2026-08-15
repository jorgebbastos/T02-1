def calcular_total(itens, desconto_percentual=0, cupom=""):

    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    cupons = {
        "vale10": 10,
        "vale5": 5
    }

    if cupom == "":
        desconto_cupom = 0
    elif cupom in cupons:
        desconto_cupom = cupons[cupom]
    else:
        raise ValueError("Cupom inválido.")

    if desconto_percentual + desconto_cupom > 100:
        raise ValueError("Desconto total maior que 100%")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    total = subtotal - (subtotal * ((desconto_percentual + desconto_cupom) / 100))

    return round(total, 2)
