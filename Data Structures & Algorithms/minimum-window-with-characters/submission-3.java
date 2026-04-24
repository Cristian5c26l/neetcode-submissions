class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";

        // Frecuencias de t
        Map<Character, Integer> freqT = new HashMap<>();
        for (char c : t.toCharArray()) {
            freqT.put(c, freqT.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> freqWin = new HashMap<>();
        int need = freqT.size(); // chars únicos que necesitamos cubrir
        int have = 0;            // chars que ya cubrimos

        int left = 0;
        int[] result = {-1, 0, 0}; // [largo, left, right]

        for (int right = 0; right < s.length(); right++) {
            // Agregar char derecho
            char c = s.charAt(right);
            freqWin.put(c, freqWin.getOrDefault(c, 0) + 1);

            // ¿Este char ya tiene freq suficiente?
            if (freqT.containsKey(c) && 
                freqWin.get(c).equals(freqT.get(c))) {
                have++;
            }

            // Ventana válida → encoge desde izquierda
            while (have == need) {
                // Actualizar resultado si es más corto
                if (result[0] == -1 || right - left + 1 < result[0]) {
                    result[0] = right - left + 1;
                    result[1] = left;
                    result[2] = right;
                }

                // Remover char izquierdo
                char leftC = s.charAt(left);
                freqWin.put(leftC, freqWin.get(leftC) - 1);
                if (freqT.containsKey(leftC) && 
                    freqWin.get(leftC) < freqT.get(leftC)) {
                    have--;
                }
                left++;
            }
        }

        return result[0] == -1 ? "" : 
            s.substring(result[1], result[2] + 1);
    }
}
