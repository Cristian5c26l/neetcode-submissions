class Solution {
    public int carFleet(int target, int[] position, int[] speed) {

        int n = position.length;

        // Tener un mapa o registro de carros, y en cada uno, registrar su posicion actual, y su correspondiente tiempo para llegar a la meta (target)
        double[][] cars = new double[n][2];
        for(int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = (double) (target - position[i])/ speed[i]; 
        }

        // Aprovechar la ventaja de la ordenacion. Podemos tener registrados los carros de modo que el primero este mas cercano a la meta (su posicion sea cercana al target). Asi, el tiempo en que llega el primero, sera el minimo requerido para que los carros que esten en las siguientes posiciones, formen una flota con el. Si estos carros llegan a un tiempo mayor a la meta, pues, estos serán parte de otras flotas.
        // (a, b) -> Double.compare(b[0], a[0]) se encarga de ordenar el cars, pero, por posicion
        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));

        Deque<Double> stack = new ArrayDeque<>();

        for(double[] car: cars) {
            double currentTime = car[1];
            if(stack.isEmpty() || currentTime > stack.peek()) {
                stack.push(currentTime);
            }
        }

        return stack.size();
    }
}
