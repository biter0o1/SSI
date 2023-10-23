import numpy as np

#zad 1
def array_of_array_of_strings_to_float(x = []):
    result = []
    for i in x:
        inside_arr = []
        for j in i:
            try:
                inside_arr.append(float(j))
            except:
                print(f'wartosci = {j} nie da sie przerobic na float')
        result.append(inside_arr)
    print(result)
    

array_of_array_of_strings_to_float([['1', 'a', '3'],['2', '4', '4.2']])


#zad 2


