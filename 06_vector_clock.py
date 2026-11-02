class Process:
    def __init__(self, pid, total):
        self.pid = pid
        self.clock = [0] * total

    def local_event(self):
        self.clock[self.pid] += 1
        print(f"P{self.pid} local event: {self.clock}")

    def send(self):
        self.clock[self.pid] += 1
        print(f"P{self.pid} sends: {self.clock}")
        return self.clock.copy()

    def receive(self, msg_clock):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], msg_clock[i])
        self.clock[self.pid] += 1
        print(f"P{self.pid} receives: {self.clock}")


def compare(a, b):
    a_before_b = all(a[i] <= b[i] for i in range(len(a))) and a != b
    b_before_a = all(b[i] <= a[i] for i in range(len(a))) and a != b
    if a_before_b:
        return "A happened before B"
    if b_before_a:
        return "B happened before A"
    return "A and B are concurrent"


p0 = Process(0, 3)
p1 = Process(1, 3)
p2 = Process(2, 3)

p0.local_event()
msg = p0.send()
p1.receive(msg)
p2.local_event()

print(compare(p1.clock, p2.clock))
print(compare(p0.clock, p1.clock))
