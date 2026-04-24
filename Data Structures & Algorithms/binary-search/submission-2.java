class Solution {
    public int search(int[] nums, int target) {// Busqueda binaria es utilizada en arrays de enteros diferentes que van de menor a mayor

        int low = 0;
        int high = nums.length - 1;
        int midIndex = (high - low) / 2;
        
        // O(logn) porque midIndex va decreciendo en mitades de n (n = high - low)
        while(midIndex >=low && midIndex <= high ){// La busqueda en el array solo estará disponible mientras el indice midIndex este entre los extremos del subarray analizado

            if(nums[midIndex] == target) {
                return midIndex;
            }

            if(target > nums[midIndex]) {
                low = midIndex + 1;
                midIndex = low + ((high - low) / 2);
            } else if(target < nums[midIndex]) {
                high = midIndex - 1;
                midIndex = low + ((high - low) / 2);
            }

        }

        return -1;

    }
}
