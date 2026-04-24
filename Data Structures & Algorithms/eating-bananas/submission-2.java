class Solution {
    public int minEatingSpeed(int[] piles, int h) {// O(n) + O(n*logm) = O(n*logm)
        
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();// O(n) E Arrays.stream(piles).max().getAsInt()
        int minRate = high;

        // O(n*logm)
        // Binary Search
        // O(logm)
        while(low <= high) {
            int k = ((low + high) / 2);// k = mid
            int kRateHours = hoursUntilEatingAllBananas(piles, k);// O(n)

            if(h >= kRateHours) {// Si las horas, en que koko puede comer todas las bananas de las pilas a una velocidad de k bananas por hora en cada pila, estan dentro de las horas h en que las puede comer, buscar otra k mas pequeña que aun sea posible de entrar dentro de esas horas h
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
            hours += (k + bananas - 1) / k;// "(k + bananas - 1) / k" permite calcular el numero de horas en las que koko comera todas las bananas de la pila actual, a una frecuencia de k bananas por hora (iteracion)
        }

        return hours;
    }
}
