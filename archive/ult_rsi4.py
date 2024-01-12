import backtrader_ult_rsi as bt

class MyStrategy(bt.Strategy):
    params = (
        ('length', 14),
        ('smo_type1', MovingAverageType.TMA),
        ('smo_type2', MovingAverageType.TMA),
        ('smooth', 14),
        ('oversold', 15),
        ('overbought', 85),
    )

    def __init__(self):
        self.arsi, self.signal = calculate_ultimate_rsi(self.data.close, self.params.length, self.params.smo_type1, self.params.smo_type2, self.params.smooth)

    def next(self):
        if crossover(self.arsi, self.signal) and self.arsi < self.params.oversold:
            self.buy(size=0.1)

        if crossover(self.signal, self.arsi) and self.arsi > self.params.overbought:
            self.sell(size=0.1)

cerebro = bt.Cerebro()
data = bt.feeds.YahooFinanceCSVData(dataname='/path/to/your/data.csv')
cerebro.adddata(data)
cerebro.addstrategy(MyStrategy)
cerebro.run()
cerebro.plot()