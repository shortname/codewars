def cached(f):
    cache = {}
    def caching_fibonacci(n):
        if not cache.get(n):
            cache[n] = f(n)
        return cache[n]
    return caching_fibonacci

@cached
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)