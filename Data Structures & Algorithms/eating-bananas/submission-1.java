class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();
        int minRate = high;
        while(low <= high) {
            int k = ((low + high) / 2);// k = mid

            if(h >= hoursUntilEatingAllBananas(piles, k)) {
                minRate = k;
                high = k - 1;
            } else {
                low = k + 1;
            }
        }

        return minRate;
    }

    private int hoursUntilEatingAllBananas(int[] piles, int k) {//
        int hours = 0;
        for(int bananas: piles) {
            hours += (k + bananas - 1) / k;// (k + bananas - 1) / k permite calcular el numero de horas en las que koko comera todas las bananas de la pila actual, a una frecuencia de k bananas por hora (iteracion)
        }

        return hours;
    }
}
