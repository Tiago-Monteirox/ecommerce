import pdb

def formata_preco(valor):
    return f'R$ {valor:.2f}'.replace(',', '.')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_soma_total(carrinho):

    return sum([
        item['preco_quantitativo_promocional']
        if item['preco_quantitativo_promocional']
        else item['preco_quantitativo']
        for item in carrinho.values()
    ])
