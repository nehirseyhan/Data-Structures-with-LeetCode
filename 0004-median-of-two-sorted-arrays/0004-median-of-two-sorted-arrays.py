class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l = len(nums1) + len(nums2)
        mer = []
        p1 = 0
        p2 = 0
        x = 0
        if len(nums1) and len(nums2):
            while x < l:
                if nums1[p1] <= nums2[p2]:
                    mer.append(nums1[p1])
                    p1 = p1 + 1
                else:
                    mer.append(nums2[p2])
                    p2 = p2 + 1
                if p1 == len(nums1):
                    flag = 1
                    break
                if p2 == len(nums2):
                    flag = 2
                    break
                x = x+1
            if flag == 1:
                while p2 < len(nums2):
                    mer.append(nums2[p2])
                    p2 = p2+1
            if flag == 2:
                while p1 < len(nums1):
                    mer.append(nums1[p1])
                    p1 = p1+1
            if len(mer) % 2 == 1:
                return mer[(len(mer)-1)/2]
            if len(mer) % 2 == 0:          
                return (float(mer[len(mer)/2]) + mer[len(mer)/2 - 1])/2
        if len(nums1) == 0:
            if len(nums2) % 2 == 1:
                return nums2[(len(nums2)-1)/2]
            if len(nums2) % 2 == 0:          
                return (float(nums2[len(nums2)/2]) + nums2[len(nums2)/2 - 1])/2
        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[(len(nums1)-1)/2]
            if len(nums1) % 2 == 0:          
                return (float(nums1[len(nums1)/2]) + nums1[len(nums1)/2 - 1])/2
           
        

