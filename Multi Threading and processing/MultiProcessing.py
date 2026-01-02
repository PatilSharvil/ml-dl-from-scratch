# process that runs in parallel -> multiprocessing
# in cpu bound tasks we can use multiprocessing 
# Parallel execution Multiple cores of the CPU

import time
import multiprocessing

def Square_numbers() : 
    for i in range(5) : 
        time.sleep(1)
        print(f'sqaure : {i * i}')
        
def Cube_numbers() : 
    for i in range(5) : 
        time.sleep(1.5)
        print(f'Cube : {i * i * i}')
        
if __name__ == '__main__' : 
# create 2 process
    p1 = multiprocessing.Process(target=Square_numbers)
    p2 = multiprocessing.Process(target=Cube_numbers)  

    t = time.time()

    # Start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join() 

    finished_time = time.time() - t
    print(f'{finished_time}')