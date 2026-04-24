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

        List<String> decoded = new ArrayList<>();

        while(i < encodedSize) {

            int j = i;
            //String sizeEncodedSubstr = "";
            StringBuilder sizeEncodedSubstr = new StringBuilder();


            while(str.charAt(j) != '#') {
                //sizeEncodedSubstr += String.valueOf(str.charAt(j));
                sizeEncodedSubstr.append(str.charAt(j));
                j++;
            }

            i = j + 1;

            int k = 0;
            //String decodedSubstr = "";// It could be a string builder for a better performance of a string changing many times. String is immutable while StringBuilder is mutable.
            
            StringBuilder decodedSubstr = new StringBuilder();
            
            while(k < Integer.parseInt(sizeEncodedSubstr.toString())) {
                
                decodedSubstr.append(str.charAt(i));

                k++;
                i++;
            }

            decoded.add(decodedSubstr.toString());
        }


        return decoded;


    }
}
