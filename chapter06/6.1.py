from queue import Queue

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= BUCKETS
        print("step", d + 1, A)

import random

BUCKETS = 10
DIGITS = 4
data = []
for i in range(10):
    data.append(random.randint(1, 9999))

print("Initial Data:", data)
radix_sort(data)
print("Radix Sorted Data:", data)