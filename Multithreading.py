import threading
import numpy as np
import time
import multiprocessing
import matplotlib.pyplot as plt

def matrix_multiplication(start,end,fixed_matrix,random_matrices,result):
    for i in range (start,end):
        result[i] = np.dot(fixed_matrix,random_matrices[i])

def main(num_threads):
    num_matrices = 100
    matrix_size = (1000,1000)
    num_rows,num_cols = matrix_size

    
    random_matrices = [np.random.rand(num_rows,num_cols) for _ in range(num_matrices)]
    fixed_matrices = np.random.rand(num_rows,num_cols)

    result = [None]*num_matrices

    chunk_size = num_matrices // num_threads

    threads = []

    for i in range(num_threads):
        start = i*chunk_size
        end = start+chunk_size if i<num_threads-1 else num_matrices
        thread = threading.Thread(target = matrix_multiplication,args=(start,end,fixed_matrices,random_matrices,result))
        threads.append(thread)

    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Multiplication with {num_threads} threads took {end_time - start_time} seconds.")   

if __name__ == "__main__":
    num_threads = [1, 2, 3, 4,5,6,7,8]  # Test different numbers of threads
    for num_thread in num_threads:
        main(num_thread)