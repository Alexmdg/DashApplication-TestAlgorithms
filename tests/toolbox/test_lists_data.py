import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from AlgoWebSite.DashApps.toolbox.list_datas import *

class Test_Data():
    list1 = Data([0, 1, 2])
    list2 = Data([5, 4])

    def test_Data_init(self):
        errors=[]
        if self.list1.datas != [0, 1, 2]:
            errors.append('self.data error')
        if print(self.list1) != print('[0, 1, 2]'):
            errors.append('repr error')
        if not self.list2 < self.list1:
            errors.append('cmp error')
        assert len(errors) == 0

    def test_sort_by_insertion(self):
        self.list2.insert_sort_time = self.list2._sort_by_insertion()[1]
        errors=[]
        if self.list2.sorted_datas is None and self.list2.insert_sort_time is None:
            errors.append(f'function returned nothing')
        elif self.list2.sorted_datas != [4, 5]:
            errors.append(f'data not sorted well : {self.list2.sorted_datas}')
        elif type(self.list2.insert_sort_time) != type(float()):
            errors.append(f'time error : {self.list2.insert_sort_time}')
        assert len(errors) == 0

    def test_sort_by_merging(self):
        self.list2.merge_sort_time = self.list2._sort_by_merging()[1]
        errors=[]
        if self.list2.sorted_datas is None and self.list2.merge_sort_time is None:
            errors.append(f'function returned nothing')
        elif self.list2.sorted_datas != [4, 5]:
            errors.append(f'data not sorted well : {self.list2.sorted_datas}')
        elif type(self.list2.merge_sort_time) != type(float()):
            errors.append(f'time error : {self.list2.merge_sort_time}')
        assert len(errors) == 0

    def test_sort_by_heapify(self):
        self.list2.heapify_sort_time = self.list2._sort_by_heapify()[1]
        errors=[]
        if self.list2.sorted_datas is None and self.list2.heapify_sort_time is None:
            errors.append(f'function returned nothing')
        elif self.list2.sorted_datas != [4, 5]:
            errors.append(f'data not sorted well : {self.list2.sorted_datas}')
        elif type(self.list2.insert_sort_time) != type(float()):
            errors.append(f'time error : {self.list2.insert_sort_time}')
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
        if self.data_set._datas != [self.list2, self.list1, self.list3]:
            errors.append('self.datas error')
        if self.data_set.raw_datas != self.data_set._datas:
            errors.append('self.raw_datas error')
        assert len(errors) == 0

    def test_run_tests(self):
        self.data_set.run_tests('insert', 'merge', 'heapify')
        errors = []
        for datas in self.data_set.raw_datas:
            if datas.sorted_datas is None and datas.insert_sort_time is None:
                errors.append(f'function returned nothing for {datas}')
        if type(self.data_set.insert_sort_time) is not type(float()):
            errors.append(f'self.data_set.insert_sort_time error : {self.data_set.insert_sort_time}')
        if type(self.data_set.merge_sort_time) is not type(float()):
            errors.append(f'self.data_set.merge_sort_time error: {self.data_set.merge_sort_time}')
        if type(self.data_set.heapify_sort_time) is not type(float()):
            errors.append(f'self.data_set.heapify_sort_time error : {self.data_set.heapify_sort_time}')
        assert len(errors) == 0

