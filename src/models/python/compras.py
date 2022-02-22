

class Compra:
    
    def __init__(self, data_c: str, data_e: str, qtd: int ) -> None:
        """Define uma compra

        Parameters
        ----------
        data_c : str
            data da compra
        data_e : str
            data da entrega
        qtd : int
            quantidade prevista
        """        
        self.data_c = data_c
        self.data_e = data_e 
        self.qtd = qtd 
        self.realizada = False