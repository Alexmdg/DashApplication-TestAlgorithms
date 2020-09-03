import math, random
import numpy as np
from multiprocessing import pool
import concurrent.futures
#######################################################################################
# This file contains all algorithmic pure functions used on lists :
#
# generateListe(n) : with 'n' an integer,
#                    generate a list of length 'n'
#
# insertSort(liste) : with 'liste' a list of integer,
#                     sorts 'liste' by insertion method and returns the sorted list
#
# mergeSort(myList) : with 'myList' a list of integer,
#                     sorts 'myList' by merging method and returns the sorted list
#
# binarySearch(liste, x) : with 'liste' a sorted list of integer and 'x' an integer,
#                          returns the position of 'x' in 'list'
#######################################################################################
test = False


#TODO######################################################################################
#TODO#
#TODO#                         COMPLEXITY ALGORITHMES
#TODO#
#TODO######################################################################################


def generateListe(n):
    liste = [random.randint(0, 3 * n) for _ in range(n)]
    return liste

#######################################################################################

def generateListes(size, step):
    i = 2
    listes = []
    while i < size:
        i = int(i * float(step))
        listes.append(generateListe(i))
    return listes


#TODO#####################################################################################
#TODO#
#TODO#                         SORTING ALGORITHMES
#TODO#
#TODO#####################################################################################


def insertSort(my_list):
    sorted_liste = [x for x in my_list]
    for j in range(len(sorted_liste)):
        i = j
        while i > 0:
            if sorted_liste[i] < sorted_liste[i - 1]:
                tmp = sorted_liste[i]
                sorted_liste[i] = sorted_liste[i - 1]
                sorted_liste[i - 1] = tmp
            else:
                break
            i -= 1
    return sorted_liste

#######################################################################################

def mergeSort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
    return my_list

def multiThreadMerging(my_list):
    if len(my_list) > 1024:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(mergeSort, [left, right])
        sides = [result for result in results]
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if sides[0][i] < sides[1][j]:
                my_list[k] = sides[0][i]
                i += 1
            else:
                my_list[k] = sides[1][j]
                j += 1
            k += 1
        while i < len(sides[0]):
            my_list[k] = sides[0][i]
            i += 1
            k += 1
        while j < len(sides[1]):
            my_list[k] = sides[1][j]
            j += 1
            k += 1
    else:
        mergeSort(my_list)
    return my_list

def multiprocMerging(my_list):
    pass



#TODO######################################################################################
#TODO#
#TODO#                         MAXIMUM SUB ARRAY ALGORITHMES
#TODO#
#TODO######################################################################################


def varListe(liste):
    var_liste = list(range(len(liste)))
    i = 1
    while i < len(liste):
        var_liste[i] = liste[i] - liste[i - 1]
        i += 1

    return var_liste

#######################################################################################

def maxTabCroise(var_liste, bas, haut):
    haut = haut
    max_var = var_liste[0]
    var = 0
    for i in range(len(var_liste)):
        var = var + var_liste[i]
        if var >= max_var:
            max_var = var
            haut = i

    bas = bas
    var = 0
    max_var = 0
    for i in range(len(var_liste[:haut]), -1, -1):
        var = var + var_liste[i]
        if var >= max_var:
            max_var = var
            bas = i

    return bas, haut, max_var

#######################################################################################

def maxTabDnR(var_liste, bas, haut):
    if len(var_liste) == 1:
        var = var_liste[0]
        return bas, haut, var

    elif len(var_liste) == 0:
        var = 0
        return bas, haut, var

    else:

        mid = (bas + haut) // 2
        left_tab = [x for x in var_liste[:(len(var_liste) // 2)]]
        right_tab = [x for x in var_liste[(len(var_liste) // 2):]]

        bas_left, haut_left, var_left = maxTabDnR(left_tab, bas, mid)
        bas_right, haut_right, var_right = maxTabDnR(right_tab, mid + 1, haut)

        range_croise = [x for x in var_liste[bas_left - bas:haut_right - bas + 1]]
        bas_croise, haut_croise, var_croise = maxTabCroise(range_croise, bas_left - bas, haut_right - bas)

        if var_croise >= max(var_left, var_right):
            var = var_croise
            bas = bas_croise + bas_left
            haut = haut_croise + bas_left

        elif var_left >= var_right:
            bas = bas_left
            haut = haut_left
            var = var_left

        elif var_left < var_right:
            bas = bas_right
            haut = haut_right
            var = var_right

        return bas, haut, var



#TODO######################################################################################
#TODO#
#TODO#                         TABLES ALGORITHMES
#TODO#
#TODO######################################################################################

def generateTab(n, m):
    tab = np.array([[random.randint(0, 3 * n) for _ in range(n)] for i in range(m)], dtype=np.int)
    return tab

def simple_matrix_product(tab1, tab2):
    if len(tab1) != len(tab2[0]) or len(tab1[0]) != len(tab2):
        return 'les tableaux doivent être de forme n*m et m*n'
    else:
        tab=np.zeros((len(tab1[0]), len(tab1[0])), dtype=np.int)
        sum_liste=[0] * len(tab)
        tmp_liste=[0] * len(tab)
        for k in range(0, len(tab)):
            for i in range(0, len(tab1[0])):
                for j in range(0, len(tab2[0])):
                    sum_liste[j] = tab1[k][j] * tab2[j][i]
                tmp_liste[i]=sum(sum_liste)
            tab[k] = [x for x in tmp_liste]
        return tab


def recursiv_matrix_product(tab1, tab2):
    if len(tab1) != len(tab2[0]) or len(tab1[0]) != len(tab2):
        return 'les tableaux doivent être de forme n*m et m*n'
    elif math.log(len(tab1[0]), 2) != int(math.log(len(tab1[0]), 2)):
        return "les nombres de lignes et de colones doivent être une puissance de 2"
    else:
        def recursiv_algo(tab1, tab2):

            a = len(tab1)
            b = a // 2

            tab = np.zeros((a, a), dtype=np.int)
            if a == 1:
                return tab1 * tab2
            else:
                tab[0:b, 0:b] = recursiv_algo(tab1[0:b, 0:b], tab2[0:b, 0:b]) \
                                + recursiv_algo(tab1[0:b, b:a], tab2[b:a, 0:b])
                tab[0:b, b:a] = recursiv_algo(tab1[0:b, 0:b], tab2[0:b, b:a]) \
                                + recursiv_algo(tab1[0:b, b:a], tab2[b:a, b:a])
                tab[b:a, 0:b] = recursiv_algo(tab1[b:a, 0:b], tab2[0:b, 0:b]) \
                                + recursiv_algo(tab1[b:a, b:a], tab2[b:a, 0:b])
                tab[b:a, b:a] = recursiv_algo(tab1[b:a, 0:b], tab2[0:b, b:a]) \
                                + recursiv_algo(tab1[b:a, b:a], tab2[b:a, b:a])
            return tab
        return recursiv_algo(tab1, tab2)

def stressen_matrix_multiplication(tab1, tab2):
    def stressen_algo(tab1, tab2):
        a = len(tab1)
        b = a // 2
        tab = np.zeros((a, a), dtype=np.int)

        if a == 4:
            return simple_matrix_product(tab1, tab2)
        else:
            m1 = stressen_algo(tab1[:b, :b] + tab1[b:, b:], tab2[:b, :b]+tab2[b:, b:])
            m2 = stressen_algo(tab1[b:, :b] + tab1[b:, b:], tab2[:b, :b])
            m3 = stressen_algo(tab1[:b, :b], tab2[:b, b:] - tab2[b:, b:])
            m4 = stressen_algo(tab1[b:, b:], tab2[b:, b:] - tab2[:b, :b])
            m5 = stressen_algo(tab1[:b, :b] + tab1[:b, b:], tab2[b:, b:])
            m6 = stressen_algo(tab1[b:, :b] - tab1[:b, :b], tab2[:b, :b] + tab2[:b, b:])
            m7 = stressen_algo(tab1[:b, b:] - tab1[b:, b:], tab2[b:, :b] + tab2[b:, b:])

            tab[:b ,:b] = m1 + m2 - m5 + m7
            tab[:b, b:] = m3 + m5
            tab[b:, :b] = m2 + m4
            tab[b:, b:] = m1 - m2 + m3 + m6
        return tab
    return stressen_algo(tab1, tab2)


#TODO######################################################################################
#TODO#
#TODO#                         TREES ALGORITHMES
#TODO#
#TODO######################################################################################




#!#########################################################################################
#!#
#!#                                TEST ZONE
#!#
#!#########################################################################################
if __name__ == '__main__':
    # test = True

#!# TEST COMPLEXITY ALGOS #!#

    # size = input('size :')
    # step = input('step :')
    # listes = generateListes(int(size), float(step))
    # datas = insertSort(listes)
    # data2={'x': [],
    #        'y': []}
    # i=2
    # while i < int(size):
    #     i = int(i*float(step))
    #     result, timing = mergeSort(generateListe(i))
    #     data2['x'].append(len(result))
    #     data2['y'].append(timing)
    #
    #
    # x1 = [dic['x'] for dic in datas]
    # y1 = [dic['y'] for dic in datas]
    # x2=data2['x']
    # y2=data2['y']
    #
    # # datas2 = mergeSort(listes)
    # # datas= [datas1, datas2]
    # print('x1 : {}'.format(x1))
    # print('y1 : {}'.format(y1))
    # print('x2 : {}'.format(x2))
    # print('y2 : {}'.format(y2))
    # fig = go.Figure()
    # fig.add_scatter(x=x1, y=y1, line={'shape':'spline'})
    # fig.add_scatter(x=x2, y=y2, line={'shape':'spline'})
    # # fig=px.line(x=[x1, x2], y=[y1, y2], line_shape='spline')
    # fig.show()

#!# TEST SORTING ALGOS #!#

    import multiprocessing

    print(multiprocessing.cpu_count())
    n = 1000000
    # result = []
    # listes = [
    #     [0, 7, -27, 8, -15, 45, 29, -85, 11, 7, 65, -8, 2, 5, -17, -12, \
    #      -10, 9, -44, 59, -7, -22, 39, -73, 11, -16, 16, -1, 73, -71, -2, 42, -6],
    #     [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2],
    #     [12, 99, 99, -99, -27, 0, 0, 0, -3, 10],
    #     [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11],
    #     [31, -41, 59, 26, -53, 58, 97, -93, -23, 84],
    # ]
    # liste = [0] * n
    #
    # for i in range(n):
    #     liste[i] = random.randint(0, 3 * n)
    #
    # a = time.time()
    # liste = insertSort(liste)
    # b = time.time()
    # result.append({'test': 'insertSort',
    #                'Taille liste': n,
    #                'time': (b-a),
    #                })
    #

    liste = [random.randint(0, 3 * n) for _ in range(n)]
    liste = multiThreadMerging(liste)
    print(liste)
    # b = time.time()
    # result.append({'test': 'mergeSort',
    #                'Taille liste': n,
    #                'time': (b-a),
    #                })
    #
    # for i in range(n):
    #     liste[i] = random.randint(0, 3 * n)
    # a = time.time()
    # var_liste = varListe(liste)
    # b = time.time()
    # result.append({'test': 'varListe',
    #                'Taille liste': n,
    #                'time': (b - a),
    #                })
    #
    # a = time.time()
    # bas, haut, var = maxTabDnR(var_liste, 0, len(var_liste) - 1)
    # b = time.time()
    # result.append({'test': 'maxTabDnR',
    #                'liste': [x for x in var_liste[bas:haut]],
    #                'bas': bas, 'haut': haut, 'var': var,
    #                'time': (b - a),
    #                })
    #
    # for dict in result:
    #     print(dict)

# !# TEST TABLE ALGOS #!#

    # tab1 = (generateTab(4, 4))
    # tab2 = (generateTab(4, 4))
    #
    # print('tab1 : {}'.format(tab1))
    # print('tab2 : {}'.format(tab2))
    # print('sum tab : {}'.format(tab1+tab2))
    # print(recursiv_matrix_product(tab1, tab2))
    # print(simple_matrix_product(tab1, tab2))
    # print(stressen_matrix_multiplication(tab1, tab2))
    #
    # print(recursiv_matrix_product(tab1, tab2))
