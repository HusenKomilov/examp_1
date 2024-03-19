# 1-masala
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(map(str, digits)))
        c = str(a + 1)
        m = [int(i) for i in c]
        return m


# 2-masala
class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        base = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in base.values():
                a.append(i)
            elif i in base.keys():
                if not a or base[i] != a.pop():
                    return False
            else:
                return False

        return not a
