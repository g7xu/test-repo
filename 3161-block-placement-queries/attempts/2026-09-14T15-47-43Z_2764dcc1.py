import bisect

class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        blocks = [0, float('inf')]
        res = []

        for query in queries:
            if query[0] == 1:
                bisect.insort(blocks, query[1])
            else:
                for i in range(1, len(blocks)):
                    if blocks[i] > query[1]:
                        if query[1] - blocks[i - 1] >= query[2]:
                            res.append(True)
                        else:
                            res.append(False)
                        
                        break
                    
                    if blocks[i] - blocks[i - 1] >= query[2]:
                        res.append(True)
                        break

        return res


        
        
