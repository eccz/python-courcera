import copy
import sys


class Matrix:
    def __init__(self, mlist):
        self.copy = copy.deepcopy(mlist)

    def __str__(self):
        all_str = ''
        for elem in self.copy:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str.strip()

    def size(self):
        return len(self.copy), len(self.copy[0])

    def __add__(self, other):
        all_str = ''
        for i, e in enumerate(self.copy):
            for j, k in enumerate(e):
                all_str += f'{k + other.copy[i][j]}\t'
            all_str += '\n'
        return all_str.strip()

    def __mul__(self, other):
        all_str = ''
        for i, e in enumerate(self.copy):
            for j, k in enumerate(e):
                all_str += f'{k * other}\t'
            all_str += '\n'
        return all_str.strip()

    __rmul__ = __mul__


exec(sys.stdin.read())
