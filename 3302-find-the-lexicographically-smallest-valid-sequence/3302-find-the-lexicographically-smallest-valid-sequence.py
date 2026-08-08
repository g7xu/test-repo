class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        @cache
        def helper(i, j, change_count):
            
            if j >= len(word2):
                return []

            if i >= len(word1):
                return None

            if word1[i] == word2[j]:
                tmp = helper(i+1, j+1, change_count)
                if tmp is not None:
                    return [i] + tmp
                else:
                    return helper(i+1, j, change_count)

            if change_count != 0:
                tmp = helper(i+1, j+1, change_count - 1)
                if tmp is not None:
                    return [i] + tmp
                
            return helper(i+1, j, change_count)

        res = helper(0, 0, 1)

        if res is None:
            return []

        return res

            

