from main import Data, Plot, np

if __name__ == '__main__':
    obiekt_z_danymi = Data('lab1/iris.txt', names=['sepal_length_in_cm', 'sepal_width_in_cm', 'petal_length_in_cm', 'petal_width_in_cm', 'class'])

    data = obiekt_z_danymi.get_data()

    plot = Plot()


    # <lab2-zad3>
    plot.wykres_okrag_rysuj()

    plot.wykres_punkty_rysuj_2([-0.5, 0, 0.5], [0.2, 0, 0.2], color='blue', marker='D')

    plot.wykres_linie_rysuj_x_y(np.linspace(-0.75, 0.75 , 7), np.sin([0, -0.1, -0.2, -0.2, -0.2, -0.1, 0]), color='yellow')

    plot.show()
    # </lab2-zad3>

    # <lab2-zad4>
    setosa = data[data['class'] == 1]
    versicolour = data[data['class'] == 2]
    virginica = data[data['class'] == 3]

    plot.subplot(2, 2, 1)
    plot.wykres_punkty_rysuj_2(setosa['petal_length_in_cm'], setosa['petal_width_in_cm'], color='blue', label='Setosa', marker='o')
    plot.wykres_punkty_rysuj_2(versicolour['petal_length_in_cm'], versicolour['petal_width_in_cm'], color='yellow', label='Versicolour', marker='x')
    plot.wykres_punkty_rysuj_2(virginica['petal_length_in_cm'], virginica['petal_width_in_cm'], color='green', label='Virginica', marker='s')


    plot.subplot(2, 2, 2)
    plot.wykres_punkty_rysuj_2(setosa['sepal_width_in_cm'], setosa['petal_width_in_cm'], color='blue', label='Setosa', marker='o')
    plot.wykres_punkty_rysuj_2(versicolour['sepal_width_in_cm'], versicolour['petal_width_in_cm'], color='yellow', label='Versicolour', marker='x')
    plot.wykres_punkty_rysuj_2(virginica['sepal_width_in_cm'], virginica['petal_width_in_cm'], color='green', label='Virginica', marker='s')


    plot.subplot(2, 2, 3)
    plot.wykres_punkty_rysuj_2(setosa['sepal_length_in_cm'], setosa['petal_width_in_cm'], color='blue', label='Setosa', marker='o')
    plot.wykres_punkty_rysuj_2(versicolour['sepal_length_in_cm'], versicolour['petal_width_in_cm'], color='yellow', label='Versicolour', marker='x')
    plot.wykres_punkty_rysuj_2(virginica['sepal_length_in_cm'], virginica['petal_width_in_cm'], color='green', label='Virginica', marker='s')

    plot.subplot(2, 2, 4)
    plot.wykres_punkty_rysuj_2(setosa['sepal_width_in_cm'], setosa['petal_length_in_cm'], color='blue', label='Setosa', marker='o')
    plot.wykres_punkty_rysuj_2(versicolour['sepal_width_in_cm'], versicolour['petal_length_in_cm'], color='yellow', label='Versicolour', marker='x')
    plot.wykres_punkty_rysuj_2(virginica['sepal_width_in_cm'], virginica['petal_length_in_cm'], color='green', label='Virginica', marker='s')
    # </lab2-zad4>

    plot.show()