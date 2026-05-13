import time
from functools import wraps


def memoize(max_size=None, policy='lru', ttl=None, custom_evict=None):
    def decorator(func):
        cache = {}
        usage_order = []
        usage_count = {}
        created_at = {}
        
        def make_key(args, kwargs):
            return args + tuple(sorted(kwargs.items()))
        
        def evict_if_needed():
            if max_size is None or len(cache) <= max_size:
                return
            
            if custom_evict is not None:
                key_to_remove = custom_evict(cache)
            
            elif policy == 'lfu':
                key_to_remove = min(usage_count, key=lambda key: usage_count[key])
            else:
                key_to_remove = usage_order[0]
                
            cache.pop(key_to_remove, None)
            usage_count.pop(key_to_remove, None)
            created_at.pop(key_to_remove, None)
            
            if key_to_remove in usage_order:
                usage_order.remove(key_to_remove)
                
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            now = time.time()
            
            if key in cache:
                if ttl is not None and now - created_at[key] > ttl:
                    cache.pop(key, None)
                    usage_count.pop(key, None)
                    created_at.pop(key, None)
                    
                    if key in usage_order:
                        usage_order.remove(key)
                else:
                    usage_count[key] += 1
                    
                    if key in usage_order:
                        usage_order.remove(key)
                        
                    usage_order.append(key)
                    return cache[key]
                
            result = func(*args, **kwargs)
            
            cache[key] = result
            usage_count[key] = 1
            created_at[key] = now
            usage_order.append(key)
            
            evict_if_needed()
            
            return result
        return wrapper
    return decorator
