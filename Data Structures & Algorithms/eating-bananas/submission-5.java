class Solution {
    public int minEatingSpeed(int[] piles, int h) {// O(n) + O(n*logm) = O(n*logm)
        
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();// O(n) E Arrays.stream(piles).max().getAsInt()
        int minRate = high;

        // O(n*logm)
        // Binary Search
        while (low <= high) {// O(logm)
            int k = low + ((high - low) / 2);// k = mid... (low + high / 2 tambien podria ser k)
            int kRateHours = hoursUntilEatingAllBananas(piles, k);// O(n)

            if (h >= kRateHours) {// Si las horas, en que koko puede comer todas las bananas de las pilas a una velocidad de k bananas por hora (iteracion) en cada pila, estan dentro de las horas h en que las puede comer, buscar otra k mas pequeña que aun sea posible de entrar dentro de esas horas h
                minRate = k;
                high = k - 1;
            } else {// Si en cambio las horas en las que koko se come todas las bananas son mayores a h (tarda mas de las horas requeridas), hacer que la proxima k (numero de bananas comidas por hora-iteracion en cada pila) sea mayor a la actual analizada
                low = k + 1;
            }
        }

        return minRate;
    }

    private int hoursUntilEatingAllBananas(int[] piles, int k) {// O(n)
        int hours = 0;
        for(int bananas: piles) {
            hours += (k + bananas - 1) / k;// "(k + bananas - 1) / k" permite calcular el numero de horas en las que koko comera todas las bananas de la pila actual, a una frecuencia de k bananas por hora (iteracion)
        }

        return hours;
    }
}
