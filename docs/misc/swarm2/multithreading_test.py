import numpy as np
import time

start_time = time.time()

a = np.random.randn(5000, 50000)
b = np.random.randn(50000, 5000)
ran_time = time.time() - start_time
print("time to complete random matrix generation was %s seconds" % ran_time)

np.dot(a, b) #this line is multithreaded
print("time to complete dot was %s seconds" % (time.time() - start_time - ran_time))
