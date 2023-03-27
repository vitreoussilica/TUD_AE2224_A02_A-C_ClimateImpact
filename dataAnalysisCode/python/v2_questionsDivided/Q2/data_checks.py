import flight

def is_full_set(flight_triplet: list):    
    ## Then check that the optimisation of each flight is different
    ## And check that all other fields are the same
    for i in range(0,3):
        for j in range(0,3):
            if i != j:
                if flight_triplet[i].optimisation == flight_triplet[j].optimisation:
                    return False
                if flight_triplet[i].datestamp != flight_triplet[j].datestamp:
                    return False
                if flight_triplet[i].day != flight_triplet[j].day:
                    return False
                if flight_triplet[i].time != flight_triplet[j].time:
                    return False
                if flight_triplet[i].route != flight_triplet[j].route:
                    return False
    return True