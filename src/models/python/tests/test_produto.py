import sys
from typing import List

from produto import Produto

def test_produto() -> bool:

    produtos : List[Produto] = []  
    produtos.append(Produto("Mesa", "Uma mesa"))
    produtos.append(Produto("Cadeira", "Uma cadeira"))
    produtos.append(Produto("Sofa", "Um sofá"))

    for produto in produtos:
        print("Produto: "+produto.nome_curto+" | Descrição: "+produto.descricao+" | id: "+str(produto.id))

    return True


    