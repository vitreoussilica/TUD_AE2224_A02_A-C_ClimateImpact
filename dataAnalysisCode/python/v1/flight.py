class Flight:
    def __init__(self, data, datestamp, day, time, optimisation, route):
        self.data = data
        self.datestamp = datestamp
        self.day = day
        self.time = time
        self.optimisation = optimisation
        self.route = route

    def total_ATR(self):
        return self.data[15,:].sum()

