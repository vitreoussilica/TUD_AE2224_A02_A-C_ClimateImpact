import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er
import data_checks as checks
import triplet_generation as tg
import emission_species as es

import xarray as x

routes_list = er.all_route_coordinates()

NOX_Ozone = es.NOX_Ozone()
NOX_Methane = es.NOX_Methane()
Water_Vapour = es.Water_Vapour()
Contrails = es.Contrails()
CO2 = es.CO2()
Total = es.Total()

triplets = tg.all_triplets()

progress_counter = 0

for triplet in triplets:
    SOCs = [triplet[0].total_SOC(), triplet[1].total_SOC(), triplet[2].total_SOC()]

    NOX_Ozone.add_triplet_data_specific(triplet, SOCs)
    NOX_Methane.add_triplet_data_specific(triplet, SOCs)
    Water_Vapour.add_triplet_data_specific(triplet, SOCs)
    Contrails.add_triplet_data_specific(triplet, SOCs)
    CO2.add_triplet_data_specific(triplet, SOCs)
    Total.add_triplet_data_specific(triplet, SOCs)
    if count % 50 == 0:
        print (f'{round(count / 79000 * 100)}%', end="\r")
    progress_counter += 1

NOX_Ozone.print_files('NOX_Ozone')
NOX_Methane.print_files('NOX_Methane')
Water_Vapour.print_files('Water_Vapour')
Contrails.print_files('Contrails')
CO2.print_files('CO2')
Total.print_files('Total')