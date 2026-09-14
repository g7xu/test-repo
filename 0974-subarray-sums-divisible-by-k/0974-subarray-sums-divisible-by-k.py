class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc = [0]
        res = 0

        for num in nums:
            acc.append(acc[-1] + num)

        for i in range(1, len(acc)):
            for j in range(i, len(acc)):
                if (acc[j] - acc[i - 1]) % k == 0:
                    res += 1

        return res
