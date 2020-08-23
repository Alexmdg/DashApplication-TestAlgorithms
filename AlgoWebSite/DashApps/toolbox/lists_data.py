from prelog import CheckLog
from prelog import FORMATS
from prelog import LEVELS as poglevel
import heapq

log = CheckLog(fmt=FORMATS['locate'])
log.main.setLevel(poglevel['1'])
log.dataProc.setLevel(poglevel['1'])
log.dataIO.setLevel(poglevel['1'])
log.display.setLevel(poglevel['1'])


class Data:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return (len(self.data) < len(other.data))

    def __repr__(self):
        return str(self.data)


class DataSet:
    def __init__(self):
        self.raw_datas=[]
        self.datas = []

    def add(self, new_data):
        heapq.heappush(self.raw_datas, new_data)

    def sort(self):
        self.datas = [heapq.heappop(self.raw_datas) for _ in range(len(self.raw_datas))]
        self.raw_datas = self.datas


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
    print(A.data)