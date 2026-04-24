class Solution {
    public int search(int[] nums, int target) {// Busqueda binaria es utilizada en arrays de enteros diferentes que van de menor a mayor

        int low = 0;
        int high = nums.length - 1;
        
        // O(logn) porque midIndex va decreciendo en mitades de n (n = high - low)
        while(low <= high ){// La busqueda en el array solo estará disponible mientras el indice midIndex este entre los extremos del subarray analizado

            int midIndex = low + ((high - low) / 2);

            if(nums[midIndex] == target) {
                return midIndex;
            } else if(target > nums[midIndex]) {
                low = midIndex + 1;
            } else if(target < nums[midIndex]) {
                high = midIndex - 1;
            }

        }

        return -1;

    }
}
