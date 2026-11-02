processes = [1, 2, 3, 4, 5]   # process IDs arranged in a ring
alive = {1: True, 2: True, 3: True, 4: True, 5: False}   # 5 (old leader) crashed


def ring_election(starter):
    n = len(processes)
    start_index = processes.index(starter)
    election_list = [starter]
    print(f"Process {starter} starts election")

    i = (start_index + 1) % n
    while processes[i] != starter:
        if alive[processes[i]]:
            print(f"Process {starter} -> Process {processes[i]}")
            election_list.append(processes[i])
        i = (i + 1) % n

    leader = max(election_list)
    print("Election list:", election_list)
    print("New leader (coordinator):", leader)


ring_election(2)
