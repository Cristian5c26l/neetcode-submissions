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
        for (String[] entry : map.get(key)) {
            int storedTime = Integer.parseInt(entry[1]);
            if (storedTime <= timestamp) {
                result = entry[0]; // más reciente válido
            }
        }

        return result;
    }
}
