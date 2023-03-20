class Flight:
    def __init__(self, data, datestamp, day, time, optimisation, route):
        self.data = data
        self.datestamp = datestamp
        self.day = day
        self.time = time
        self.optimisation = optimisation
        self.route = route


    def total_ATR_NOX_Ozone(self):
        return self.data[10,:].sum()
    
    def total_ATR_NOX_Methane(self):
        return self.data[11,:].sum()
    
    def total_ATR_Water_Vapour(self):
        return self.data[12,:].sum()
    
    def total_ATR_Contrails(self):
        return self.data[13,:].sum()
    
    def total_ATR_CO2(self):
        return self.data[14,:].sum()
    
    def total_ATR(self):
        return self.data[15,:].sum()

    
    def print_summary(self):
        print(f'Flight data shape: {self.data.shape}')
        print(f'Month: {self.datestamp}')
        print(f'Day: {self.day}')
        print(f'Time: {self.time}')
        print(f'Optimisation: {self.optimisation}')
        print(f'Route: {self.route}')

