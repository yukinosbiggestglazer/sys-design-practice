# Clock times in minutes
master_time = 180
slave_times = {"Slave1": 170, "Slave2": 190, "Slave3": 200}

# Step 1: master collects differences
diffs = {"Master": 0}
for name, time in slave_times.items():
    diffs[name] = time - master_time

print("Differences from master:", diffs)

# Step 2: calculate average difference
average = sum(diffs.values()) / len(diffs)
print("Average difference:", average)

# Step 3: calculate adjustment for each machine
for name, diff in diffs.items():
    adjustment = average - diff
    print(f"{name}: adjust by {adjustment}")
