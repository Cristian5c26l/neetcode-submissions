class Solution {
    public String minWindow(String s, String t) {

        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();

        for(char c: t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
            window.put(c, window.getOrDefault(c, 0));
        }

        int left = 0;
        int right = 0;
        int slidingWindow;
        int valid = 0;
        int min = 9999999;

        //StringBuilder substr = new StringBuilder("");
        String substr = "";
        while(right < s.length()) {

            char c = s.charAt(right);

            if(!need.containsKey(c)) {
                right++;
                continue;
            }

            window.replace(c, window.getOrDefault(c, 0) + 1);

            if(need.get(c) == window.get(c)) {
                valid += 1;
            }

            if(valid == need.size()) {
                
                System.out.println("Substr: "+ s.substring(left, right + 1));

                while(valid == need.size()) {

                    char car = s.charAt(left);

                    if(!need.containsKey(car)) {
                        left++;
                        continue;
                    }

                    window.replace(car, window.getOrDefault(car, 0) - 1);

                    if(need.get(car) > window.get(car)) {
                        valid--;
                    }

                    slidingWindow = right + 1 - left;

                    if(slidingWindow < min) {
                        min = slidingWindow;
                        substr = s.substring(left, right + 1);
                    }

                    left++;


                }

                System.out.println("Substr quedado (continua right++): "+ s.substring(left, right + 1));

            }

            right++;
        }

        return substr;
    }
}
