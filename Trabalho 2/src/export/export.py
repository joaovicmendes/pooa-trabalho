class Export:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self, articles):
        self._strategy.execute(articles)
