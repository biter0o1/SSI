import numpy as np

import matplotlib.pyplot as plt

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

wzorce = [bitmapa_wzorcowa_1, bitmapa_wzorcowa_2, bitmapa_wzorcowa_3]

## 1
wyniki_podobienstwa_1 = [miara_podobienstwa_obustronnego(bitmapa_testowa_1, wzorzec) for wzorzec in wzorce]

print(f'Bitmapa testowa 1. Najwiekszy wynik = najbardziej podobna: {wyniki_podobienstwa_1}')

plt.figure(figsize=(12, 8), dpi=80)

plt.subplot(3, 2, 1)
plt.imshow(bitmapa_testowa_1, cmap='Greys')

plt.subplot(3, 2, 2)
plt.imshow(wzorce[np.argmax(wyniki_podobienstwa_1)], cmap='Greys')


## 2
wyniki_podobienstwa_2 = [miara_podobienstwa_obustronnego(bitmapa_testowa_2, wzorzec) for wzorzec in wzorce]

print(f'Bitmapa testowa 2. Najwiekszy wynik = najbardziej podobna: {wyniki_podobienstwa_2}')

plt.subplot(3, 2, 3)
plt.imshow(bitmapa_testowa_2, cmap='Greys')

plt.subplot(3, 2, 4)
plt.imshow(wzorce[np.argmax(wyniki_podobienstwa_2)], cmap='Greys')


## 3
wyniki_podobienstwa_3 = [miara_podobienstwa_obustronnego(bitmapa_testowa_3, wzorzec) for wzorzec in wzorce]

print(f'Bitmapa testowa 3. Najwiekszy wynik = najbardziej podobna: {wyniki_podobienstwa_3}')

plt.subplot(3, 2, 5)
plt.imshow(bitmapa_testowa_3, cmap='Greys')

plt.subplot(3, 2, 6)
plt.imshow(wzorce[np.argmax(wyniki_podobienstwa_3)], cmap='Greys')

plt.show()