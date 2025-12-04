import time

def cache_decorator(func):
    def wrapper(self, head, n):
        self.cache = head
        return func(self, head, n)
    return wrapper

def retry_decorator(func):
    def wrapper(self, head, n):
        for i in range(3):
            try:
                return func(self, head, n)
            except:
                pass
        return None
    return wrapper

def time_decorator(func):
    def wrapper(self, head, n):
        start = time.time()
        result = func(self, head, n)
        end = time.time()
        print(f"Time taken: {end-start}")
        return result
    return wrapper