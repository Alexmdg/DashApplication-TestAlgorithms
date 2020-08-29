import prelog as pog
import heapq

from DashApps.algos.Dunod.list_sorting import *

log = pog.CheckLog(fmt=pog.FORMATS['locate'])
log.main.setLevel(pog.LEVELS['1'])
log.dataProc.setLevel(pog.LEVELS['1'])
log.dataIO.setLevel(pog.LEVELS['1'])
log.display.setLevel(pog.LEVELS['1'])


class Data:
    def __init__(self, data):
        self.datas = data
        self.sorted_datas = None
        self.insert_sort_time = None
        self.merge_sort_time = None
        self.heapify_sort_time = None

    def __lt__(self, other):
        return (len(self.datas) < len(other.datas))

    def __repr__(self):
        return str(self.datas)

    @pog.timer
    def _sort_by_insertion(self):
        self.sorted_datas = [item for item in self.datas]
        self.sorted_datas = insertSort(self.sorted_datas)

    @pog.timer
    def _sort_by_merging(self):
        self.sorted_datas = [item for item in self.datas]
        self.sorted_datas = mergeSort(self.sorted_datas)

    @pog.timer
    def _sort_by_heapify(self):
        self.heap = [item for item in self.datas]
        heapq.heapify(self.heap)
        self.sorted_datas = [heapq.heappop(self.heap) for _ in range(len(self.heap))]


class DataSet:
    def __init__(self):
        self.raw_datas=[]
        self._datas = []

    def add(self, new_data):
        heapq.heappush(self.raw_datas, new_data)

    def sort(self):
        self._datas = [heapq.heappop(self.raw_datas) for _ in range(len(self.raw_datas))]
        self.raw_datas = self._datas

    def run_tests(self, *algos):
        if 'insert' in algos:
            self.insert_sort_time = 0
            for datas in self.raw_datas:
                datas.insert_sort_time = datas._sort_by_insertion()[1]
                self.insert_sort_time += datas.insert_sort_time
        if 'merge' in algos:
            self.merge_sort_time = 0
            for datas in self.raw_datas:
                datas.merge_sort_time = datas._sort_by_merging()[1]
                self.merge_sort_time += datas.merge_sort_time
        if 'heapify' in algos:
            self.heapify_sort_time = 0
            for datas in self.raw_datas:
                datas.heapify_sort_time = datas._sort_by_heapify()[1]
                self.heapify_sort_time += datas.heapify_sort_time



if __name__ == '__main__':
    datas = DataSet()
    A = Data([0, 1, 2, 100])
    B = Data([1, 2])
    C = Data([1000])
    datas.add(A)
    datas.add(B)
    datas.add(C)
    datas.sort()
    log.dataIO.cmn_dbg(datas.datas)
    print(A)