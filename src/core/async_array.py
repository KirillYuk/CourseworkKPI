import asyncio


def async_filter_callback(items, predicate, callback, delay=0):
    async def runner():
        result = []
        for item in items:
            if delay:
                await asyncio.sleep(delay)
            if await predicate(item):
                result.append(item)
        callback(result)
        
    return asyncio.create_task(runner())

async def async_filter(items, predicate, cancel_event=None, delay=0):
    result = []
    for item in items:
        if cancel_event is not None and cancel_event.is_set():
            break
        
        if delay:
            await asyncio.sleep(delay)
            
        if await predicate(item):
            result.append(item)
            
    return result