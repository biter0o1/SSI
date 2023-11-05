import math
import random
import matplotlib.pyplot as plt

class Evolutionary_algorithm():

    def funkcja_przystosowania(self, x):
        return math.sin(x / 10) * math.sin(x / 200)

    def run(self, rozrzut, wsp_przyrostu, iteracje, zakres_zmienności):
        x = random.uniform(zakres_zmienności[0], zakres_zmienności[1])
        y = self.funkcja_przystosowania(x)

        x_calego_zakresu = [i for i in range(zakres_zmienności[0], zakres_zmienności[1] + 1)]
        y_calego_zakresu = [self.funkcja_przystosowania(x) for x in x_calego_zakresu]

        plt.figure(figsize=(12, 8), dpi=80)
        plt.plot(x_calego_zakresu, y_calego_zakresu, label='Funkcja przystosowania')

        for i in range(iteracje):
            xpot = x + random.uniform(-rozrzut, rozrzut)
            
            xpot = max(zakres_zmienności[0], min(zakres_zmienności[1], xpot))

            ypot = self.funkcja_przystosowania(xpot)
            if ypot >= y:
                x = xpot
                y = ypot
                rozrzut *= wsp_przyrostu
            else:
                rozrzut /= wsp_przyrostu

            print(f'Nr iter: {i}, x: {x}, y: {y}, rozrzut: {rozrzut}')

            plt.plot(x, y, self.plot_style()[i % 8], label=f'x={x:.2f}, y={y:.2f}')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def plot_style(self):
        return ['rX', 'gX', 'bX', 'cX', 'mX', 'yX', 'kX', 'wX']
        


if __name__ == '__main__':
    ea = Evolutionary_algorithm()
    ea.run(10, 1.1, 100, (0, 100))