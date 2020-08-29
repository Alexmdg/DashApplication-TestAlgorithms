from prelog import CheckLog
from prelog import FORMATS
from prelog import LEVELS as poglevel
import heapq
from AlgoWebSite.DashApps.algos.Dunod.list_sorting import *

log = CheckLog(fmt=FORMATS['locate'])
log.main.setLevel(poglevel['1'])
log.dataProc.setLevel(poglevel['1'])
log.dataIO.setLevel(poglevel['1'])
log.display.setLevel(poglevel['1'])


class Data:
    def __init__(self, data):
        self.data = data
        self.sorted_data = []

    def __lt__(self, other):
        return (len(self.data) < len(other.data))

    def __repr__(self):
        return str(self.data)

    def _sort_by_insertion(self):
        # self.sorted_data =


class DataSet:
    def __init__(self):
        self.raw_datas=[]
        self._datas = []

    def add(self, new_data):
        heapq.heappush(self.raw_datas, new_data)

    def sort(self):
        self._datas = [heapq.heappop(self.raw_datas) for _ in range(len(self.raw_datas))]
        self.raw_datas = self._datas


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