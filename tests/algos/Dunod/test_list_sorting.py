import unittest
import pytest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)

from AlgoWebSite.DashApps.algos.Dunod.list_sorting import *

class Test_ListGenerator:
    n = 10

    def test_generateList(self):
        random_list = generateListe(self.n)
        errors=[]
        if len(random_list) != self.n:
            errors.append(f'{random_list}')
        else:
            for item in random_list:
                if type(item) is not type(int()):
                    errors.append(type(item))
        assert len(errors) == 0


class Test_listSort:
    my_list = [5, 3, 8, 4]
    my_other_list = [5, 11, 3, 8, 4]

    # def test_insertSort(self):
    #     sorted_list = insertSort(self.my_list)
    #     other_sorted_list = insertSort(self.my_other_list)
    #     errors = []
    #     if sorted_list != [3, 4, 5, 8]:
    #         errors.append(f'list not sorted: {sorted_list}')
    #     if other_sorted_list != [3, 4, 5, 8, 11]:
    #         errors.append(f'list not sorted: {other_sorted_list}')
    #     assert len(errors)==0

    def test_mergeSort(self):
        sorted_list = mergeSort(self.my_list)
        other_sorted_list = mergeSort(self.my_other_list)
        errors = []
        if sorted_list != [3, 4, 5, 8]:
            errors.append(f'list not sorted: {sorted_list}')
        if other_sorted_list != [3, 4, 5, 8, 11]:
            errors.append(f'list not sorted: {other_sorted_list}')
        assert len(errors) == 0








