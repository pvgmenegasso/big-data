import math
from typing import List
from models.python.estoque import Estoque


class CD:
    
    def __init__(self, capacidade: int, estoques: List[Estoque]) -> None:
        '''Define um centro de distribuição

        Parameters
        ----------
        capacidade : int
            capacidade max de armazenamento em nr de produtos
        estoques : List[Estoque]
            uma lista dos estoques 
        '''              
        self.capacidade = capacidade
        self.estoques = estoques
        total_produtos = 0
        for produto in estoques:
            total_produtos += produto.quantidade
        self.qtd_produtos_armazenados = total_produtos

    def get_uso(self) -> int:
        '''Retorna a porcentagem do espaço de armazenamento do 
        CD que foi utilizada até o momento

        Returns
        -------
        int
            uso do CD em %
        '''        
        return round((self.qtd_produtos_armazenados/self.capacidade)*100)

    def add_estoque(self, estoque: Estoque) -> None:
        '''Adiciona ume estoque ao CD

        Parameters
        ----------
        estoque : Estoque
            O estoque a ser adicionado
        '''        
        self.estoques = self.estoques.append(estoque)

    def get_estoque(self) -> List[Estoque]:
        '''Retorna a lista de estoques

        Returns
        -------
        List[Estoque]
            Os estoques contidos no CD
        '''        
        return self.estoques

            
            