import math


class MinHeap(object):
    def __repr__(self):
        return str(self.values)

    def __init__(self, values=[]):
        self.values = []
        for v in values:
            self.push(v)

    def _swap(self, i, j):
        i_val = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = i_val

    def pop(self):
        if not self.values:
            raise Exception("empty heap")

        if len(self.values) == 1:
            r = self.values[0]
            self.values = []
            return r

        r = self.values[0]
        last = self.values[-1]
        self.values[0] = last
        self.values = self.values[:-1]

        imbalanced = True
        i = 0
        while imbalanced:
            left = 2*i + 1
            right = 2*i + 2
            if left > len(self.values) - 1:
                break
                # no left

            if right > len(self.values) - 1:
                # no right
                self._swap(i, right)
                break

            if self.values[left] < self.values[right]:
                child_index = left
            else:
                child_index = right
            self._swap(i, child_index)
            i = child_index

        return r

    def push(self, value):
        self.values.append(value)
        i = len(self.values) - 1
        parent_index = math.floor((i-1)/2)
        if self.values[i] < self.values[parent_index]:
            imbalanced = True
        else:
            imbalanced = False

        while imbalanced:
            self._swap(i, parent_index)
            i = parent_index
            parent_index = math.floor(parent_index / 2)
            if self.values[i] >= self.values[parent_index]:
                imbalanced = False

