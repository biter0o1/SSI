import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Data:
    def __init__(self, path: str, names = None):
        self._data = pd.read_csv(path, delim_whitespace=True, header=None, names=names)  

    def get_data(self):
        return self._data
    
    def print_x_y(self, x, y):
        print(self._data.values[x][y])

    def get_data_x_y(self, x, y):
        print(self._data.loc[x, y])


class Plot:
    def plot_style(self):
        return ['rD', 'gX', 'bo', 'r^', 'bv', 'r2', 'ys', 'b*', 'rx', 'r|']

    def subplot(self, x = 1, y = 1, number = 1):
        plt.subplot(x, y, number)

    def wykres_czysc(self):
        plt.clf()

    def wykres_linie_rysuj_x(self, x = [], color='red', linestyle='solid', label='x'):
        plt.plot(x, label=label, color=color, linestyle=linestyle)

    def wykres_linie_rysuj_x_y(self, x = [], y = [], color='red', linestyle='solid', label='x'):
        plt.plot(x, y, label=label, color=color, linestyle=linestyle)

    def wykres_punkty_rysuj(self, x = [], y = [], style_index = 0):
        plt.plot(x, y, self.plot_style()[style_index])

    def wykres_punkty_rysuj_2(self, x = [], y = [], color='red', marker='o', label='Punkty danych'):
        plt.scatter(x, y, color=color, marker=marker, label=label)

    def wykres_okrag_rysuj(self):
        theta = np.linspace(0, 2 * np.pi, 15)
        circle_x = np.cos(theta)
        circle_y = 0.4 * np.sin(theta)
        self.wykres_linie_rysuj_x_y(circle_x, circle_y, label='circle')

    def show(self):
        plt.grid(True)
        plt.xlabel('Oś X')
        plt.ylabel('Oś Y')
        plt.title('plot')
        plt.legend(loc='upper right', bbox_to_anchor=(1, 1.15))
        plt.show()

    def test(self):
        pass
