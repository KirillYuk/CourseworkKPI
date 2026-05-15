import asyncio
import logging
import time
from functools import wraps


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

def log(level="INFO"):
    def decorator(func):
        
        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                start = time.time()
                
                try:
                    result = await func(*args, **kwargs)
                    
                    if level in ("INFO", "DEBUG"):
                        logging.log(
                            getattr(logging, level),
                            "%s args=%s kwargs=%s result=%s duration=%s",
                            func.__name__,
                            args,
                            kwargs,
                            result,
                            round(time.time() - start, 4)
                            )
                    return result
                
                except Exception as error:
                    logging.error(
                        "%s error=%s duration=%s",
                        func.__name__,
                        error,
                        round(time.time() - start, 4)
                        )
                    raise
                
            return async_wrapper
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            
            try:
                result = func(*args, **kwargs)
                
                if level in ("INFO", "DEBUG"):
                    logging.log(
                        getattr(logging, level),
                        "%s args=%s kwargs=%s result=%s duration=%s",
                        func.__name__,
                        args,
                        kwargs,
                        result,
                        round(time.time() - start, 4)
                        )
                    
                return result
            
            except Exception as error:
                logging.error(
                    "%s error=%s duration=%s",
                    func.__name__,
                    error,
                    round(time.time() - start, 4)
                    )
                raise
            
        return wrapper
    
    return decorator
