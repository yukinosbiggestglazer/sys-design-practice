import threading 
import time

threads = []

mat = [[1, 2, 0, 1], [0, 1, 3, 2], [2, 0, 1, 1], [1, 1, 0, 2]]
ans = [[0] * 4 for i in range(4)]


def compute_row (name, row):
	global mat, ans
	for i in range(4):
		o = 0
		for j in range(4):
			o += mat[row][j] * mat[j][i]
		ans[row][i] = o
		time.sleep(0.1)
	print(name, "did row ", row)


for i in range(4):
	t = threading.Thread(target=compute_row, args=("Th-" + str(i), i,))
	threads.append(t)
	
for t in threads:
	t.start()
	
for t in threads:
	t.join()
	
print(ans)
