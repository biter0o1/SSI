import numpy as np
from main import Plot, Data
import matplotlib.pyplot as plt

#zad 1
# def array_of_array_of_strings_to_float(x = []):
#     result = []
#     for i in x:
#         inside_arr = []
#         for j in i:
#             try:
#                 inside_arr.append(float(j))
#             except:
#                 print(f'wartosci = {j} nie da sie przerobic na float')
#         result.append(inside_arr)
#     print(result)
    

# array_of_array_of_strings_to_float([['1', 'a', '3'],['2', '4', '4.2']])


#zad 2

class KMeans():

    def __init__(self, data):
        self.data = data

    def calculate_distance(self, sample_1, sample_2):
        return ((sample_1 - sample_2) ** 2).sum() ** 0.5
    
    def run(self, plot=None):
        k = 4

        centroids = self.data.sample(n=k)

        initial_centroids = centroids.copy()

        iterations = 100
        for i in range(iterations):
            clusters = [[] for _ in range(k)]
            for s in range(len(self.data)):
                distances = []
                for j in range(len(centroids)):
                    distance = self.calculate_distance(self.data.loc[s], centroids.iloc[j])
                    distances.append(distance)

                cluster_index = np.argmin(distances)
                clusters[cluster_index].append(s)

                for j in range(k):
                    if len(clusters[j]) > 0:
                        centroids.iloc[j] = self.data.loc[clusters[j]].mean()

            if i == 0:
                plt.figure(figsize=(10, 6))
                plot.subplot(1, 2, 1)
                plot.wykres_punkty_rysuj_2(self.data.iloc[clusters[0], 0], self.data.iloc[clusters[0], 1], color='green', label='grupa 1')
                plot.wykres_punkty_rysuj_2(self.data.iloc[clusters[1], 0], self.data.iloc[clusters[1], 1], color='red', label='grupa 2')
                plot.wykres_punkty_rysuj_2(self.data.iloc[clusters[2], 0], self.data.iloc[clusters[2], 1], color='yellow', label='grupa 3')
                plot.wykres_punkty_rysuj_2(self.data.iloc[clusters[3], 0], self.data.iloc[clusters[3], 1], color='pink', label='grupa 4')
                plot.wykres_punkty_rysuj_2(initial_centroids['x'], initial_centroids['y'], color='blue', marker='X', label='Centroidy')
                plt.legend()
                plt.title('Pierwsza iteracja')
        return clusters, centroids
            



    
if __name__ == '__main__':
    obiekt_z_danymi = Data('lab3/spirala.txt', names=['x', 'y'])

    data = obiekt_z_danymi.get_data()


    plot = Plot()

    k_means = KMeans(data)

    clusters, centroids = k_means.run(plot)


    plot.subplot(1, 2, 2)

    plot.wykres_punkty_rysuj_2(data.iloc[clusters[0], 0], data.iloc[clusters[0], 1], color='green', label='grupa 1')
    plot.wykres_punkty_rysuj_2(data.iloc[clusters[1], 0], data.iloc[clusters[1], 1], color='red', label='grupa 2')
    plot.wykres_punkty_rysuj_2(data.iloc[clusters[2], 0], data.iloc[clusters[2], 1], color='yellow', label='grupa 3')
    plot.wykres_punkty_rysuj_2(data.iloc[clusters[3], 0], data.iloc[clusters[3], 1], color='pink', label='grupa 4')

    plot.wykres_punkty_rysuj_2(centroids['x'], centroids['y'], color='blue', marker='X', label='Centroidy')

    plt.legend()
    plt.title('Ostatnia iteracja')
    plt.xlabel('x')
    plt.xlabel('y')
    plt.show()
