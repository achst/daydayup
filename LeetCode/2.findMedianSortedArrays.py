"""
寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
"""

# 普通解法 O(m + n / 2)
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total % 2 == 0:
            idx1, idx2 = (total - 2) / 2, total / 2
        else:
            idx1 = idx2 = (total - 1) / 2
        idx1, idx2 = int(idx1), int(idx2)
        nums3 = []
        i = j = 0
        while (i + j) <= idx2:
            if i >= m and j < n:
                nums3.extend(nums2[j:])
                break
            elif j >= n and i < m:
                nums3.extend(nums1[i:])
                break
            else:
                if nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
        return float(nums3[idx1] + nums3[idx2]) / 2
