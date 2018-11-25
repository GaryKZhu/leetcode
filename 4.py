class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        combined = []
        combined.extend(nums1)
        combined.extend(nums2)
        combined = sorted(combined)
        length = len(combined)
        if length % 2 != 0:
            return combined[length // 2]
        else:
            return (combined[length // 2-1] + combined[length//2]) / 2
