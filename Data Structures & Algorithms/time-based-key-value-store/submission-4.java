class TimeMap {

    private Map<String, List<String[]>> map;

    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        List<String[]> keyList = map.getOrDefault(key, new ArrayList<>());
        keyList.add(new String[]{value, String.valueOf(timestamp)});
        map.put(key, keyList);
    }
    
    public String get(String key, int timestamp) {

        if (!map.containsKey(key)) return "";

        String result = "";
        List<String[]> content = map.get(key);

        int low = 0;
        int high = content.size() - 1;
        while(low <= high) {
            
            int mid = low + ((high - low) / 2);
            String[] entry = content.get(mid);// feelingTimestamp = entry
            int storedTime = Integer.parseInt(entry[1]);
            
            if(storedTime <= timestamp) {
                result = entry[0];
                low = mid + 1;
            } else {
                high = mid - 1;
            }

        }

        return result;
    }
}
