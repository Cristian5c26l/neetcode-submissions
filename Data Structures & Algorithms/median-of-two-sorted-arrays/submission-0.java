class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        // O(|m - n|)
        int[] fullArray = IntStream.concat(Arrays.stream(nums1), Arrays.stream(nums2)).toArray();
        
        // O(nlogn)
        Arrays.sort(fullArray);

        System.out.println("Array full: " + Arrays.toString(fullArray));

        if(fullArray.length % 2 == 0) {
            return (double) ((fullArray[fullArray.length / 2] + fullArray[(fullArray.length / 2) - 1] ) / 2.0);
        }

        return fullArray[fullArray.length / 2]; 
    }
}
