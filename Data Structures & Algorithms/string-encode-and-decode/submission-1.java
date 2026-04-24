class Solution {

    public String encode(List<String> strs) {
        
        StringBuilder encodedSb = new StringBuilder();
        
        for(String str: strs) {
            encodedSb.append(str.length() + "#");
            encodedSb.append(str);
        }

        return encodedSb.toString();
    }

    public List<String> decode(String str) {

        int encodedSize = str.length();
        int i = 0;

        //String decoded = "";
        List<String> decoded = new ArrayList<>();

        while(i < encodedSize) {

            int j = i;
            String sizeEncodedSubstr = "";

            while(str.charAt(j) != '#') {
                sizeEncodedSubstr += String.valueOf(str.charAt(j));
                j++;
            }

            i = j + 1;

            int k = 0;
            String decodedSubstr = "";
            while(k < Integer.parseInt(sizeEncodedSubstr)) {
                
                decodedSubstr += String.valueOf(str.charAt(i));
                k++;
                i++;
            }

            //decoded += substr;
            decoded.add(decodedSubstr);
        }


        return decoded;


    }
}
