import numpy as np
import random, time
from Algo.chap2.services.sortlist import generateListe


class MonTas:

    def __init__(self, liste):

        self.tas = [None]
        self.rank = {}
        for item in liste:
            self.push(item)

    def __len__(self):
        return len(self.tas)

    def push(self, item):
        self.tas.append(item)
        self.rank[item] = len(self.tas)
        self.up(len(self.tas) - 1)

    def pop(self):
        item = self.tas[1]
        self.tas[1] = self.tas[-1]
        del self.rank[item]
        del self.tas[-1]
        self.rank[self.tas[1]] = 1
        self.down(1)
        return item

    def up(self, i):
        j = i // 2
        while i > 1 and self.tas[i] < self.tas[j]:
            tmp = self.tas[i]
            self.tas[i] = self.tas[j]
            self.tas[j] = tmp
            self.rank[self.tas[i]] = i
            self.rank[self.tas[j]] = j
            j = j // 2
            i = i // 2

    def down(self, i):
        if len(self.tas) >= 2 * i:
            left = i * 2
            right = (i * 2) + 1

            while i * 2 <= len(self.tas):
                if right <= len(self.tas):
                    if self.tas[i] > self.tas[left] or self.tas[i] > self.tas[right]:
                        if self.tas[left] > self.tas[right]:
                            tmp = self.tas[right]
                            self.tas[right] = self.tas[i]
                            self.tas[i] = tmp
                            self.rank[self.tas[right]] = (i * 2) + 1
                            self.rank[self.tas[i]] = i
                        else :
                            tmp = self.tas[left]
                            self.tas[left] = self.tas[i]
                            self.tas[i] = tmp
                            self.rank[self.tas[left]] = (i * 2) + 1
                            self.rank[self.tas[i]] = i
                    i *= 2
                else :
                    if self.tas[i] > self.tas[left]:
                        tmp = self.tas[left]
                        self.tas[left] = self.tas[i]
                        self.tas[i] = tmp
                        self.rank[self.tas[left]] = (i * 2) + 1
                        self.rank[self.tas[i]] = i
                    i *= 2

                left = i * 2
                right = (i * 2) + 1




#!#########################################################################################
#!#
#!#                                TEST ZONE
#!#
#!#########################################################################################
if __name__ == '__main__':
    test = True

#!# TEST CLASS MonTas #!#

    liste = generateListe(6)
    tas = MonTas(liste)
    print(liste)
    print(tas.tas)
    print(tas.rank)
    print(tas.pop())
    # print(tas.tas)
    # print(tas.rank)
    # tas.push(2)
    # print(tas.tas)
    # print(tas.rank)
