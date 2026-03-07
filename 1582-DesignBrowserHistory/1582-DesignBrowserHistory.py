# Last updated: 3/6/2026, 9:31:37 PM
class BrowserHistory:

    def __init__(self, homepage:str):
        self.curr = Browsed(homepage)

    def visit(self, url:str) -> None:
        new_visit = Browsed(url)
        self.curr.next = new_visit
        new_visit.prev = self.curr
        self.curr = new_visit
    
    def back(self, steps:int) -> str:
        i = 0
        while self.curr:
            if i == steps:
                return self.curr.url
            i+=1
            if self.curr.prev:
                self.curr = self.curr.prev
        return None

    def forward(self, steps:int) -> str:
        i = 0
        while self.curr:
            if i == steps:
                return self.curr.url
            i+=1
            if self.curr.next:
                self.curr = self.curr.next
        return None
        
class Browsed:
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev