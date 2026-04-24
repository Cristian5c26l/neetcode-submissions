class Solution {
    public int evalRPN(String[] tokens) {
        
        Stack<Integer> stack = new Stack<>();

        for(String token: tokens) {
            
            Character c = token.charAt(0);

            if(isNumber(token)) {
                stack.push(Integer.parseInt(token));
                continue;
            }
            
            //if(stack.isEmpty()) {
            //    return false;
            //}

            int a, b, result;
            b = stack.pop();
            a = stack.pop();
            if(c.equals('+')) {
                result = a + b;
                stack.push(result);
            } else if(c.equals('-')) {
                result = a - b;
                stack.push(result);
            } else if(c.equals('*')) {
                result = a * b;
                stack.push(result);
            } else if(c.equals('/')) {
                result = a / b;
                stack.push(result);
            }// else {
            //    return false;
            //}

            

        }

        return stack.peek();

    }

    private boolean isNumber(String token) {
        try {
            Integer.parseInt(token);
            return true;
        }catch(NumberFormatException e) {
            return false;
        }
    }
}
