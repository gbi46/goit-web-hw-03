from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
import time

def factorize_number(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def factorize_sync(*numbers):
    return [factorize_number(n) for n in numbers]

def factorize_parallel(*numbers):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        results = executor.map(factorize_number, numbers)
    return list(results)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    print(cpu_count())
    
    parallel_start_time = time.time()
    results_parallel = factorize_parallel(*numbers)
    parallel_time = time.time() - parallel_start_time

    start_time = time.time()
    results_sync = factorize_sync(*numbers)
    sync_time = time.time() - start_time

    print(f"sync script time: {sync_time:.4f} seconds")
    print(f"parallel script time: {parallel_time:.4f} seconds")

    a, b, c, d  = results_parallel

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Results are correct")
