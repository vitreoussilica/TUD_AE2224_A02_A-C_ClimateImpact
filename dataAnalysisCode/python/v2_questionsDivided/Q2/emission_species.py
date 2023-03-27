import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er
import data_checks as checks
import triplet_generation as tg
import deltas_calculation as deltas

import xarray as x

class Emission(object):
    def __init__(self):
        self.atr_delta_compromise = []
        self.atr_delta_max = []
        self.soc_delta_compromise = []
        self.soc_delta_max = []
        self.soc_atr_pair_compromise = []
        self.soc_atr_pair_max = []
        return
    
    def add_triplet_data_general(self, triplet: list, totals: list, SOCs: list):
        delta_atr = deltas.delta_ATR_x(totals)
        delta_soc = deltas.delta_SOC(SOCs)

        self.atr_delta_compromise.append(delta_atr[0])
        self.atr_delta_max.append(delta_atr[1])
        self.soc_delta_compromise.append(delta_soc[0])
        self.soc_delta_max.append(delta_soc[1])
        self.soc_atr_pair_compromise.append((delta_atr[0], delta_soc[0]))
        self.soc_atr_pair_max.append((delta_atr[1], delta_soc[1]))

        return SOCs


    def print_files(self, filename_suffix: str):
        with open(f"atr_delta_compromise_{filename_suffix}.txt", "w") as f:
            for s in self.atr_delta_compromise:
                f.write(str(s) +"\n")

        with open(f"atr_delta_max_{filename_suffix}.txt", "w") as f:
            for s in self.atr_delta_max:
                f.write(str(s) +"\n")

        with open(f"soc_delta_compromise_{filename_suffix}.txt", "w") as f:
            for s in self.soc_delta_compromise:
                f.write(str(s) +"\n")

        with open(f"soc_delta_max_{filename_suffix}.txt", "w") as f:
            for s in self.soc_delta_max:
                f.write(str(s) +"\n")

        with open(f"soc_atr_pair_compromise_{filename_suffix}.txt", "w") as f:
            for s in self.soc_atr_pair_compromise:
                f.write(str(s) +"\n")

        with open(f"soc_atr_pair_max_{filename_suffix}.txt", "w") as f:
            for s in self.soc_atr_pair_max:
                f.write(str(s) +"\n")

        
class NOX_Ozone(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR_NOX_Ozone(), triplet[1].total_ATR_NOX_Ozone(), triplet[2].total_ATR_NOX_Ozone()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)



class NOX_Methane(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR_NOX_Methane(), triplet[1].total_ATR_NOX_Methane(), triplet[2].total_ATR_NOX_Methane()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)

class Water_Vapour(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR_Water_Vapour(), triplet[1].total_ATR_Water_Vapour(), triplet[2].total_ATR_Water_Vapour()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)

class Contrails(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR_Contrails(), triplet[1].total_ATR_Contrails(), triplet[2].total_ATR_Contrails()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)

class CO2(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR_CO2(), triplet[1].total_ATR_CO2(), triplet[2].total_ATR_CO2()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)

class Total(Emission):
    def __init__(self):
        super().__init__()
        return

    def add_triplet_data_specific(self, triplet: list, SOCs: list):
        totals =      [triplet[0].total_ATR(), triplet[1].total_ATR(), triplet[2].total_ATR()]
        
        super().add_triplet_data_general(triplet, totals, SOCs)



    

