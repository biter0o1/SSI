import numpy as np
import matplotlib.pyplot as plt

class HopfieldaSiecAlgorytm:

    def inicjuj(self, n):
        return np.zeros((n, n))
    
    def przeksztalc(self, obraz):
        return [[1 if i == 1 else -1 for i in wiersz] for wiersz in obraz]

    def nauczObraz(self, wagi, obraz):
        obraz = np.array(obraz).flatten()
        n = len(wagi)

        for i in range(n):
            for j in range(n):
                wagi[i, j] += (1/n) * obraz[i] * obraz[j]

    def rozpoznajObraz(self, wagi, obraz, max_iter=10):
        obraz = np.array(obraz).flatten()
        n = len(wagi)
        for _ in range(max_iter):
            for i in range(n):
                suma = 0
                for j in range(n):
                    if i != j:
                        suma += wagi[i, j] * obraz[j]
                obraz[i] = -1 if suma <= 0 else 1
        return obraz


wzorzec_1 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

wzorzec_2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

wzorzec_3 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

testowy_1 = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
]

testowy_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

testowy_3 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1]
]

siec_hopfielda = HopfieldaSiecAlgorytm()

szerokosc = 5
wysokosc = 5
n = szerokosc * wysokosc

wagi = siec_hopfielda.inicjuj(n)

wzorzec_1 = siec_hopfielda.przeksztalc(wzorzec_1)
wzorzec_2 = siec_hopfielda.przeksztalc(wzorzec_2)
wzorzec_3 = siec_hopfielda.przeksztalc(wzorzec_3)


siec_hopfielda.nauczObraz(wagi, wzorzec_1)
siec_hopfielda.nauczObraz(wagi, wzorzec_1)
siec_hopfielda.nauczObraz(wagi, wzorzec_1)

siec_hopfielda.nauczObraz(wagi, wzorzec_2)
siec_hopfielda.nauczObraz(wagi, wzorzec_2)

siec_hopfielda.nauczObraz(wagi, wzorzec_3)
siec_hopfielda.nauczObraz(wagi, wzorzec_3)
siec_hopfielda.nauczObraz(wagi, wzorzec_3)
siec_hopfielda.nauczObraz(wagi, wzorzec_3)
siec_hopfielda.nauczObraz(wagi, wzorzec_3)


test1 = siec_hopfielda.rozpoznajObraz(wagi, testowy_1)
test1 = np.array(test1).reshape((szerokosc, wysokosc))

test2 = siec_hopfielda.rozpoznajObraz(wagi, testowy_2)
test2 = np.array(test2).reshape((szerokosc, wysokosc))

test3 = siec_hopfielda.rozpoznajObraz(wagi, testowy_3)
test3 = np.array(test3).reshape((szerokosc, wysokosc))


plt.subplot(3, 1, 1)
plt.imshow(test1, cmap='Greys')

plt.subplot(3, 1, 2)
plt.imshow(test2, cmap='Greys')

plt.subplot(3, 1, 3)
plt.imshow(test3, cmap='Greys')

plt.show()