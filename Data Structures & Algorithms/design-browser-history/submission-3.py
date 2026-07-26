class VisitedPage:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.visiting_pages_history = VisitedPage(homepage)
        self.current_page = self.visiting_pages_history

    def visit(self, url: str) -> None:
        new_visited_page = VisitedPage(url)
        new_visited_page.prev = self.current_page 
        self.current_page.next = new_visited_page
        self.current_page = self.current_page.next
        
    def back(self, steps: int) -> str:
        while steps > 0 and self.current_page.prev:
            self.current_page = self.current_page.prev
            steps -= 1 
        
        return self.current_page.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current_page.next:
            self.current_page = self.current_page.next
            steps -= 1

        return self.current_page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)