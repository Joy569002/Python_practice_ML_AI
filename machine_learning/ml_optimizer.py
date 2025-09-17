import time, tracemalloc, functools, inspect, random
from functools import lru_cache
from typing import Callable, Any

# ⏱️ Time tracker
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[⏱️ {func.__name__}] {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

# 🧠 Cache with symbolic tagging
def cacheit(maxsize=128, tag=None):
    def decorator(func):
        cached = lru_cache(maxsize=maxsize)(func)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[🧠 Cache] {tag or func.__name__} → {args}")
            return cached(*args, **kwargs)
        return wrapper
    return decorator

# 🧹 Memory profiler
def memtrack(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"[🧹 {func.__name__}] Mem: {current/1024:.2f}KB | Peak: {peak/1024:.2f}KB")
        tracemalloc.stop()
        return result
    return wrapper

# 🔁 Retry logic
def retry(n=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[🔁 Retry {i+1}] {func.__name__} failed: {e}")
                    time.sleep(delay)
            raise RuntimeError(f"[❌] {func.__name__} failed after {n} retries")
        return wrapper
    return decorator

# 🧪 Type enforcement
def enforce_types(func: Callable) -> Callable:
    sig = inspect.signature(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            expected = sig.parameters[name].annotation
            if expected != inspect.Parameter.empty and not isinstance(val, expected):
                raise TypeError(f"[🧪 TypeError] {name} should be {expected}, got {type(val)}")
        return func(*args, **kwargs)
    return wrapper

# 🧬 Noise injection (for robustness testing)
def inject_noise(level=0.01):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(X, *args, **kwargs):
            noise = level * random.random()
            print(f"[🧬 Noise] Injecting {noise:.4f}")
            return func(X + noise, *args, **kwargs)
        return wrapper
    return decorator

# 🧯 Exception handler with symbolic trace
def safe_exec(symbol="🧯"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[{symbol} {func.__name__}] Exception: {e}")
                return None
        return wrapper
    return decorator

# 🧭 Dynamic routing
def route_if(condition: Callable[[Any], bool], alt_func: Callable):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                print(f"[🧭 Route] Switching to {alt_func.__name__}")
                return alt_func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 🧤 Lazy evaluation
def lazy(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[🧤 Lazy] Deferring {func.__name__}")
        return lambda: func(*args, **kwargs)
    return wrapper

# 🧱 Batch control
def batchify(batch_size=32):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(X, *args, **kwargs):
            for i in range(0, len(X), batch_size):
                print(f"[🧱 Batch] Processing {i}:{i+batch_size}")
                func(X[i:i+batch_size], *args, **kwargs)
        return wrapper
    return decorator

# 🧰 Param introspection
def introspect(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = inspect.signature(func).parameters
        print(f"[🧰 Params] {func.__name__}: {[p for p in params]}")
        return func(*args, **kwargs)
    return wrapper

# 🧞‍♂️ Symbolic error tracing
def trace_errors(symbol="🧞‍♂️"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[{symbol} {func.__name__}] Error → {type(e).__name__}: {e}")
                raise
        return wrapper
    return decorator