import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er
import data_checks as checks
import triplet_generation as tg

import xarray as x

def delta_ATR_x(totals: list):
    if totals[0] > 0 and totals[1] > 0:
        delta_ATR_x_compromise =  -1 *  (1 - totals[1] / totals[0])
        delta_ATR_x_max = -1 * (1 - totals[2] / totals[0]) 
    elif totals[0] > 0 and totals[1] < 0:
        delta_ATR_x_compromise = -1 + totals[1] / totals[0]
        delta_ATR_x_max = -1 + totals[0] / totals[0]
    elif totals[0] > 0 and totals[2] < 0:
        delta_ATR_x_compromise = -1 *  (1 - totals[1] / totals[0])
        delta_ATR_x_max = -1 + totals[1] / totals[0]
    elif totals[0] < 0 and totals[1] < 0  and totals[2] < 0:
        delta_ATR_x_compromise = -1 * (totals[1] - totals[0]) / totals[0]
        delta_ATR_x_max = -1 * (totals[2] - totals[0]) / totals[0]
    else:
        delta_ATR_x_compromise = 0
        delta_ATR_x_max = 0

    return delta_ATR_x_compromise, delta_ATR_x_max

def delta_SOC(totals: list):
    return ((totals[1] - totals[0]) / totals[0]), ((totals[2] - totals[0]) / totals[0])