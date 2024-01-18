

import threading
import time

FREQUENCY = 100
 
# This function will be executed by each thread
def routine(num):
    # Sleeping time is proportional to the number
    time.sleep(num / FREQUENCY)  # Sleep for 'num' milliseconds
    print(num, end=" ")
 
# A function that performs sleep sort
def sleep_sort(arr):
    threads = []
 
    # Create a thread for each element in the input array
    for num in arr:
        thread = threading.Thread(target=routine, args=(num,))
        threads.append(thread)
        thread.start()
 
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
 
if __name__ == "__main__":
    # Doesn't work for negative numbers
    arr = [8, 4, 250, 15, 249, 7, 10,3]
     
    sleep_sort(arr)