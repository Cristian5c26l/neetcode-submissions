class TimeMap {

    private Map<String, List<Object>> map;

    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        List<Object> keyList = map.getOrDefault(key, new ArrayList<>());
        keyList.addAll(Arrays.asList(value, timestamp));
        // O(1)
        map.put(key, map.getOrDefault(key, keyList));
    }
    
    public String get(String key, int timestamp) {

        if(!map.containsKey(key)) {
            return "";
        }

        String storedValueS = "";
        String value = "";
        for(Object storedElement: map.get(key)) {
            
            if(storedElement instanceof String) {
                storedValueS = (String) storedElement;
                continue;
            }

            if((Integer) storedElement <= timestamp) {
                value = storedValueS;
            }
        }

        return value;
    }
}
