# Last updated: 3/25/2026, 10:47:51 AM
class Foo:

    """
    LEARNED from problem:
    1. ve ry very very very messed up solution and way  of starting this since i have no idea how to deal with multithreading
    2. will definitely come back to this after i learn threading (events, semaphore, condition, barrier etc.)

    3014 ms runtime beats 10% | 20 mb memory beats 37%
    """

    def __init__(self):
        self.first_called = False
        self.second_called = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_called = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while not self.first_called:
            pass
        printSecond()
        self.second_called = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while not self.first_called or not self.second_called:
            pass
        printThird()