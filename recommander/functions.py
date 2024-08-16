import numpy as np

def cosine_sim(a,b) :
    return np.dot(a,b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

def euclidean_distance(a,b) :
    a = np.array(a)
    b = np.array(b)

    return np.linalg.norm(a - b)

def get_most_similar(v,candidates,top_n=2) :

    idx_score_tuple_list = []

    for idx,candidate in enumerate(candidates) :
        score = cosine_sim(v,candidate)
        idx_score_tuple_list.append( (idx,score) )

    return sorted(idx_score_tuple_list,key=lambda x : -x[1])[1:top_n+1]