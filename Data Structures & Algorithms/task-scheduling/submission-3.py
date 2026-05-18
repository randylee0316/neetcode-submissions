class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = [0 for _ in range(26)]

        for i in tasks:
            d[ord(i) - ord('A')] += 1


        M = max(d)
        c = 0

        for i in d:
            c += 1 if i == M else 0



        return max(len(tasks), (M-1)*(n+1) + c)

