class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        p1 = 0
        p2 = 0
        new_list = []

        # if len(nums1) == 0 or len(nums2) == 0:
        #     return new_list
        while p1 <= len(nums1)-1 and p2 <= len(nums2) -1:
            if nums1[p1] == nums2[p2]:
                new_list.append(nums1[p1])
                # new_list.append(p2)
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
            # nums1[p1] > nums2[p2]:
                p2 += 1
        return new_list

# 1, 2, 9, 10, 14
# 1, 2, 5, 11, 14