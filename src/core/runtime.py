import time


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0

    for price in iterator:
        if time.time() > end_time:
            break
        count+=1
        print(count, price)
        time.sleep(0.1)