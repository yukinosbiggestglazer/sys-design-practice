A = [[1, 2], [3, 4], [5, 6], [7, 8]]
B = [[1, 0], [0, 1]]
num_workers = 2

# Scatter: split rows of A among the workers
rows_per_worker = len(A) // num_workers
chunks = []
for w in range(num_workers):
    start = w * rows_per_worker
    end = start + rows_per_worker
    chunks.append(A[start:end])


# Each worker multiplies its rows with B
def worker_multiply(rows, B):
    result = []
    for row in rows:
        new_row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += row[k] * B[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


partial_results = []
for w in range(num_workers):
    print(f"Worker {w} gets rows: {chunks[w]}")
    partial_results.append(worker_multiply(chunks[w], B))

# Gather: combine results from all workers
C = []
for part in partial_results:
    C.extend(part)

print("Result matrix C:", C)
