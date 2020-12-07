class Export:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self, articles):
        '''
            Recebe uma lista de 'Articles' e utiliza a estratégia 
            informada no argumentodo programa 
        '''
        self._strategy.execute(articles)
