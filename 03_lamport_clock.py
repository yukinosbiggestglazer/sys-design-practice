class Process:
    def __init__(self, name):
        self.name = name
        self.clock = 0

    def local_event(self):
        self.clock += 1
        print(f"{self.name}: local event, clock = {self.clock}")

    def send(self):
        self.clock += 1
        print(f"{self.name}: sends message, clock = {self.clock}")
        return self.clock

    def receive(self, msg_time):
        self.clock = max(self.clock, msg_time) + 1
        print(f"{self.name}: receives message, clock = {self.clock}")


p1 = Process("P1")
p2 = Process("P2")

p1.local_event()
t = p1.send()
p2.local_event()
p2.receive(t)
t = p2.send()
p1.receive(t)
