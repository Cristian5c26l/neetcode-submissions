class MinStack {

    Stack<Integer> mainStack;
    Stack<Integer> minStack;// Prefijo: usar un stack para guardar el mínimo actual al momento de agregar un elemento a la mainStack

    public MinStack() {
        this.mainStack = new Stack<>();
        this.minStack = new Stack<>();
    }
    
    public void push(int val) {
        mainStack.push(val);// O(1)
        
        if(minStack.isEmpty()) {
            minStack.push(val);// O(1)
            return;
        }

        int minNum = Math.min(minStack.peek(), val);
        minStack.push(minNum);
    }
    
    public void pop() {
        mainStack.pop();// O(1)
        minStack.pop();        
    }
    
    public int top() {
        return mainStack.peek();// O(1)
    }
    
    public int getMin() {
        // O(1)
        return minStack.peek();
    }
}
