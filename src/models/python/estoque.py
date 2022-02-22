
from models.python.produto import Produto


class Estoque:
    
    def __init__(self, quantidade: int, produto: Produto) -> None:
        """Define um determinado estoque nas lojas

        Parameters
        ----------
        quantidade : int
            quantidade daquele produto
        produto : Produto
            o objeto representando o produto
        """        
        self.quantidade = quantidade
        self.produto = produto