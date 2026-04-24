class MinStack {

    Stack<Integer> stack;

    public MinStack() {
        this.stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
    }
    
    public void pop() {
        stack.pop();        
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        int min = Integer.MAX_VALUE;
        // O(n)
        for(Integer element: stack) {
            min = Math.min(min, element);
        }

        return min;
    }
}
