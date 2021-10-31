import random
import time
import os
from multiprocessing import Pool


# count the number of random points 
# that fall in the unit circle
# out of n points
def monte_carlo_steps(n):   
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
                
        if x*x + y*y <= 1:
            count=count+1       
    
    return count


if __name__=='__main__':
    start_time = time.time()
    np = int(os.environ['SLURM_NTASKS_PER_NODE'])
    print("Number of cores allocated by slurm: ", np) 

    # Nummber of points to use for the pi estimation
    n = 10000000
    
    # each worker process gets floor(n/np) number of points to calculate pi from
    part_count = [n // np for i in range(np)]

    #Create the worker pool
    pool = Pool(processes = np)   

    # parallel map
    count = pool.map(monte_carlo_steps, part_count)

    print("Esitmated value of pi: ", sum(count)/(n*1.0)*4)
    print("Time to complete estimation was %s seconds" % (time.time() - start_time))
