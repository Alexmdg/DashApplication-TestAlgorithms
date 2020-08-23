import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from AlgoWebSite.DashApps.toolbox.lists_data import *

class Test_Data():
    list1 = Data([0, 1, 2])
    list2 = Data([5, 4])

    def test_Data(self):
        errors=[]
        if self.list1.data != [0, 1, 2]:
            errors.append('self.data error')
        if print(self.list1) != print('[0, 1, 2]'):
            errors.append('repr error')
        if not self.list2 < self.list1:
            errors.append('cmp error')
        assert len(errors) == 0

class Test_DataSet():
    list1 = Data([0, 1, 2])
    list2 = Data([5, 4])
    list3 = Data([1, 1, 1, 1, 1])
    data_set = DataSet()

    def test_DataSet_add(self):
        self.data_set.add(self.list3)
        self.data_set.add(self.list2)
        self.data_set.add(self.list1)
        errors = []
        if len(self.data_set.raw_datas) != 3:
            errors.append('raw_datas length error')
        if heapq.heappop(self.data_set.raw_datas) != self.list2:
            errors.append('pop order error')
        if heapq.heappop(self.data_set.raw_datas) != self.list1:
            errors.append('pop order error')
        if heapq.heappop(self.data_set.raw_datas) != self.list3:
            errors.append('pop order error')
        assert len(errors) == 0

    def test_DataSet_sort(self):
        self.data_set.add(self.list3)
        self.data_set.add(self.list2)
        self.data_set.add(self.list1)
        self.data_set.sort()
        errors=[]
        if self.data_set.datas != [self.list2, self.list1, self.list3]:
            errors.append('self.datas error')
        if self.data_set.raw_datas != self.data_set.datas:
            errors.append('self.raw_datas error')
        assert len(errors) == 0

