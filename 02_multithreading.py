import threading

counter = 0
lock = threading.Lock()


def increment(name):
    global counter
    for _ in range(5):
        with lock:
            counter += 1
            print(f"{name} incremented counter to {counter}")


t1 = threading.Thread(target=increment, args=("Thread-1",))
t2 = threading.Thread(target=increment, args=("Thread-2",))

t1.start()
t2.start()
t1.join()
t2.join()

print("Final counter:", counter)
