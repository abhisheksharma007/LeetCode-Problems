import time


matrix = [[1,2,3],
          [3,1,2],
          [2,3,1]]

def checkValid(matrix):
    rows = {}
    cols = {}

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            ele = matrix[i][j]
            if i not in rows:
                rows[i] = []
                
            if j not in cols:
                cols[j] = []

            if ele in rows[i] or ele in cols[j]:
                return False

            rows[i].append(ele)
            cols[j].append(ele)

    return True

def checkValid1(matrix):
    for i in matrix:
        if len(i) != len(set(i)):
            return False

    for i in zip(*matrix):
        if len(i) != len(set(i)):
            return False
        
    return True

if __name__ == "__main__":
    st = time.process_time()
    
    res = checkValid1(matrix)
    print(res)
    
    et = time.process_time()
    res = et - st
    print('CPU Execution time:', res, 'miliseconds')

