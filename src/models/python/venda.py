

class Venda():
     
    def __init__(self, rot5: float=0.0, rot_tevec: float=0.0) -> None:    
        """Parametros de vendas para simulação

        Parameters
        ----------
        rot5 : float, optional
            média móvel de venda dos útlimos 5 dias, by default 0.0
        rot_tevec : float, optional
            média móvel tevec de vendas, by default 0.0
        """
        
        self.rot5 = rot5
        self.rot_tevec = rot_tevec
    
    def set_rot5(self, rot5: float) -> None:
        self.rot5 = rot5
        
    def set_rot_tevec(self, rot_tevec: float) -> None:
        self.rot_tevec = rot_tevec

        
    