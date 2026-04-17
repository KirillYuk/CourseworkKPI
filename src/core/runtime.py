import time

def run(iterator, seconds):
    end_time = time.time() + seconds

    for price in iterator:
        if time.time() > end_time:
            break
        print(price)