class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1 + nums2)

        if len(new_list) % 2 == 0:
            first_index = new_list[len(new_list) //2 -1]
            second_index = new_list[len(new_list) //2]
            return (first_index + second_index) /2
        else:
            return new_list[len(new_list) // 2]