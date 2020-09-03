import prelog as pog
import heapq
import time
import concurrent.futures

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

    def _sort_by_insertion(self):
        a = time.time()
        self.sorted_datas = [item for item in self.datas]
        self.sorted_datas = insertSort(self.sorted_datas)
        b = time.time() - a
        return b

    def _sort_by_merging(self):
        a = time.time()
        self.sorted_datas = [item for item in self.datas]
        self.sorted_datas = mergeSort(self.sorted_datas)
        b = time.time() - a
        return b

    def _sort_by_heapify(self):
        a = time.time()
        self.heap = [item for item in self.datas]
        heapq.heapify(self.heap)
        self.sorted_datas = [heapq.heappop(self.heap) for _ in range(len(self.heap))]
        b = time.time() - a
        return b


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
            self.insert_datas = []
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = [executor.submit(datas._sort_by_insertion) for datas in self.raw_datas]
                i = 0
                for result in concurrent.futures.as_completed(results):
                    self.insert_datas.append((len(self.raw_datas[i].datas), result.result()))
                    self.raw_datas[i].insert_sort_time = self.insert_datas[i][1] * 1000
                    self.insert_sort_time += self.raw_datas[i].insert_sort_time
                    i += 1

        if 'merge' in algos:
            self.merge_sort_time = 0
            self.merge_datas = []
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = [executor.submit(datas._sort_by_merging) for datas in self.raw_datas]
                i = 0
                for result in concurrent.futures.as_completed(results):
                    self.merge_datas.append((len(self.raw_datas[i].datas), result.result()))
                    self.raw_datas[i].merge_sort_time = self.merge_datas[i][1] * 1000
                    self.merge_sort_time += self.raw_datas[i].merge_sort_time
                    i += 1
        if 'heapify' in algos:
            self.heapify_sort_time = 0
            self.heapify_datas = []
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = [executor.submit(datas._sort_by_heapify) for datas in self.raw_datas]
                i = 0
                for result in concurrent.futures.as_completed(results):
                    self.heapify_datas.append((len(self.raw_datas[i].datas), result.result()))
                    self.raw_datas[i].heapify_sort_time = self.heapify_datas[i][1] * 1000
                    self.heapify_sort_time += self.raw_datas[i].heapify_sort_time
                    i += 1



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