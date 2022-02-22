from typing import Iterable, List
from venda import Venda


class Produto:
    
    """Esta classe define um produto
    """    

    id : int = 0 

    def __init__(self, nome_curto: str, descricao: str, id: int= id) -> None:      
        """Inicializa um novo produto

        Parameters
                 
        id : int, by default Produto.id+1
            Código do produto
        nome_curto : str
            Nome do produto em formato curto
        descricao : str
            Descrição mais detalhada do produto
        """        
        self.id = __class__.id
        __class__.id = __class__.id + 1
        self.nome_curto = nome_curto
        self.descricao = descricao



    def set_prazo(self, prazo: int) -> None:
        """define o prazo acordado 

        Parameters
                 
        prazo : int
            tempo de produção do fornecedor + prazo de entrega (dias)
        """        
        self.prazo = prazo

    def set_intervalo(self, intervalo: int)  -> None:
        """Define o intervalo de entrega do produto

        Parameters
                 
        intervalo : int
            próxima entrega em + intervalo (dias)
        """        
        self.intervalo = intervalo

    def set_lote_minimo(self, lote_min: int)  -> None:
        """Define a compra mínima que o fornecedor aceita

        Parameters
                 
        lote_min : int
            Quantidade mínima que o fornecedor vende em unidades
        """        
        self.lote_min = lote_min

    def set_entrega_minima(self, entrega_min: int)  -> None:
        """Caso a compra seja fracionada em N entregas, 
        o vendedor não realizará entregas contendo menos
        que entrega_min produtos

        Parameters
                 
        entrega_min : int
            número mínimo de produtos entregues por vez (unidades)
        """        
        self.entrega_min = entrega_min

    def set_tempo_max_lote(self, tempo : int)  -> None:
        """Tempo máximo de duração inhouse do lote

        Parameters
                 
        tempo : int
            tempo em dias
        """        
        self.tempo_max_lote = tempo
        
    def set_excecoes(self, excs: List[int])  -> None:
        """Define dias da semana nos quais o fornecedor não entrega
        produtos

        Parameters
                 
        excs : List[int]
            Lista contendo o número dos dias em que não existe entrega (dia da semana de 06)
        """        
        self.excecoes = excs
        
    def set_periodo_sim(self, periodo: int)  -> None:
        """números de dias a serem simulados

        Parameters
                 
        periodo : int
            prazo da simulação em dias para o produto
        """        
        self.periodo_sim = periodo
        
    def set_vendas(self, vendas: List[Venda])  -> None:
        """Define a lista de vendas para o produto

        Parameters
                 
        vendas : list[Venda]
            lista de vendas relacionada ao produto
        """        
        self.vendas : list[Venda] = vendas
        
    def set_venda(self, venda: Venda, posicao: int)  -> None:
        """Define uma venda em um índice específico 

        Parameters
                 
        venda : Venda
            a venda a ser definida
        posicao : int
            a posicao
        """        
        self.vendas.insert(posicao, venda)
        
    def add_venda(self, venda: Venda)  -> None:
        """Adiciona uma venda no fim da lista de vendas atuais

        Parameters
                 
        venda : Venda
            A venda a ser adicionada
        """        
        self.vendas = self.vendas.append(venda)
        
        
