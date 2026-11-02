processes = [1, 2, 3, 4, 5]
alive = {1: True, 2: True, 3: True, 4: True, 5: False}   # 5 (coordinator) crashed


def bully_election(starter):
    print(f"Process {starter} starts election")
    higher_alive = []

    for p in processes:
        if p > starter:
            print(f"Process {starter} sends ELECTION to {p}")
            if alive[p]:
                print(f"Process {p} replies OK")
                higher_alive.append(p)
            else:
                print(f"Process {p} is down, no reply")

    if len(higher_alive) == 0:
        print(f"Process {starter} becomes the coordinator")
        return starter

    # a higher process takes over the election
    return bully_election(max(higher_alive))


leader = bully_election(2)
print("Final coordinator:", leader)
