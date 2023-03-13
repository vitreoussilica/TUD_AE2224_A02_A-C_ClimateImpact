class Flight:
    def __init__(self, data, datestamp, day, time, optimisation):
        self.data = data
        self.datestamp = datestamp
        self.day = day
        self.time = time
        self.optimisation = optimisation

    def total_ATR(self):
        return self.data[15,:].sum()

