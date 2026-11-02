servers = ["S1", "S2", "S3"]
jobs = ["J1", "J2", "J3", "J4", "J5", "J6", "J7"]

# ---------- Round Robin ----------
print("Round Robin:")
for i, job in enumerate(jobs):
    server = servers[i % len(servers)]
    print(f"{job} -> {server}")

# ---------- Least Connections ----------
print("\nLeast Connections:")
connections = {"S1": 0, "S2": 0, "S3": 0}

for job in jobs:
    # pick the server with the fewest active connections
    server = min(connections, key=connections.get)
    connections[server] += 1
    print(f"{job} -> {server}  | connections: {connections}")
