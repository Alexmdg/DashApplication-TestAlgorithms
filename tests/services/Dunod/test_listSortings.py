import pytest
import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from service.Dunod.listSortings import *



class ListFormTestCase(unittest.TestCase):
    datas = dict(n='10',
                 liste="[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]",
                 )
    form = ListForm(data=datas)
    form.liste = datas['liste']
    n = form.clean_n()
    liste = form.clean_liste()

    def test_form(self):
        self.assertTrue(self.form.is_valid())

    def test_clean_n(self):
        self.assertEqual(self.n, 10)

    def test_clean_liste(self):
        self.assertEqual(self.liste, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


class SortListTestCase(unittest.TestCase):

    liste = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_liste = liste
    sorted_liste.reverse()

    def test_generateListe(self):
        liste = generateListe(10)
        self.assertEqual(len(liste), 10)

    def test_insertSort(self):
        self.assertEqual(insertSort(self.liste), self.sorted_liste)


class MaxTabTestCase(unittest.TestCase):

    liste = [55, 48, 21, 29, 14, 59, 88, 3, 14, 21, 86, 78, 80, 85, 68, 56, 46,\
             55, 11, 70, 63, 41, 80, 7, 18, 2, 18, 91, 20, 18, 60, 54]

    varliste = [0, -7, -27, 8, -15, 45, 29, -85, 11, 7, 65, -8, 2, 5, -17, -12,\
                -10, 9, -44, 59, -7, -22, 39, -73, 11, -16, 16, 73, -71, -2, 42, -6]

    def test_varListe(self):
        self.assertEqual(varListe(self.liste), self.varliste)