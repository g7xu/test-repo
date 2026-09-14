class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numList = [int(ele) for ele in list(str(num))]

        best = sorted(numList, key = lambda x: -x)

        p = 0
        first = False
        tmp_best = None
        while p < len(numList):
            if best[p] != numList[p] and not first:
                tmp = numList[p]
                tmp_best = best[p]
                numList[p] = best[p]
                first = True
            elif tmp_best is not None and numList[p] == tmp_best:
                numList[p] = tmp
                break
            
            p += 1

        res = 0
        for i in range(len(numList)):
            res *= 10
            res += numList[i]
        
        return res



            
