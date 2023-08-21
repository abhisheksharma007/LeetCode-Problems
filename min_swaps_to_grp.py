import time

nums = [0,1,1,1,0,0,0,0,1,1,0] # circular array

if __name__ == "__main__":
    st = time.process_time()
    ress = []
    for i in range(100):
        ress.append(i)
    et = time.process_time()
    res = et - st
    print('CPU Execution time:', res, 'seconds')

