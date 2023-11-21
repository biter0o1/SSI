import numpy as np

def miara_niepodobienstwa(ba, bb):
    miara = 0

    for pay, row_a in enumerate(ba):
        for pax, val_a in enumerate(row_a):
            if val_a == 1:
                odl_min = np.inf
                
                for pby, row_b in enumerate(bb):
                    for pbx, val_b in enumerate(row_b):
                        if val_b == 1:
                            odl_akt = np.sqrt((pby - pay)**2 + (pbx - pax)**2)
                            odl_min = min(odl_min, odl_akt)
                miara += odl_min
    
    return miara

def miara_podobienstwa_obustronnego(ba, bb):
    return -(miara_niepodobienstwa(ba, bb) + miara_niepodobienstwa(bb, ba))

bitmapa_wzorcowa_1 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

bitmapa_wzorcowa_2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

bitmapa_wzorcowa_3 = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
]


bitmapa_testowa_1 = [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

bitmapa_testowa_2 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

bitmapa_testowa_3 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

print('Bitmapa testowa 1. Najwiekszy wynik = najbardziej podobna:')
print(miara_podobienstwa_obustronnego(bitmapa_testowa_1, bitmapa_wzorcowa_1))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_1, bitmapa_wzorcowa_2))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_1, bitmapa_wzorcowa_3))

print('\nBitmapa testowa 2. Najwiekszy wynik = najbardziej podobna:')
print(miara_podobienstwa_obustronnego(bitmapa_testowa_2, bitmapa_wzorcowa_1))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_2, bitmapa_wzorcowa_2))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_2, bitmapa_wzorcowa_3))

print('\nBitmapa testowa 3. Najwiekszy wynik = najbardziej podobna:')
print(miara_podobienstwa_obustronnego(bitmapa_testowa_3, bitmapa_wzorcowa_1))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_3, bitmapa_wzorcowa_2))
print(miara_podobienstwa_obustronnego(bitmapa_testowa_3, bitmapa_wzorcowa_3))
