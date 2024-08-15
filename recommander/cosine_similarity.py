import numpy as np

def dot(a,b) :
    vector_size = len(a)
    result = 0

    for idx in range(vector_size) :
        result += a[idx] * b[idx]

    return result

def cosine_sim(a,b) :
    return np.dot(a,b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

def euclidean_distance(a,b) :
    a = np.array(a)
    b = np.array(b)

    return np.linalg.norm(a - b)

if __name__ == "__main__" :
    arr0 = [1,2,3]
    arr1 = [2,3,4]

    result = dot(arr0,arr1)
    print(result)