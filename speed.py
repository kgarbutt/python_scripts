
## Python3
import time

start = time.time()

for i in range(1,1000001):
	'Number {} squared is {} and cubed is {}'.format(i, i**2, i**3)
	#print('Number {} squared is {} and cubed is {}'.format(i, i**2, i**3))

end = time.time()
total_time = end - start

print(total_time,'seconds')
print(total_time/60,'minutes')
