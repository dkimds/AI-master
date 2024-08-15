users = [ "괴벨스", "이사벨라", "요네프", "사이먼" ]
contents = [ "무한도전","런닝맨","바보임당","와썹우먼","9시뉴스","어제경제","3초요리", "거침없이하이킥","순풍산부인과", "슈카세계" ]

view_history = [
    [1,1,1,1,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,1],
]

user_to_idx = { x:idx for idx,x in enumerate(users) }
idx_to_user = { idx:x for idx,x in enumerate(users) }

content_to_idx = { x:idx for idx,x in enumerate(contents) }
idx_to_content = { idx:x for idx,x in enumerate(contents) }

def decode_matrix(matrix) :
    result = []

    for user_view_history in matrix :
        user_view_history_decoded = []

        for idx,value in enumerate(user_view_history) :

            if value == 1 :
                content_name = idx_to_content[idx]
                user_view_history_decoded.append(content_name)

        result.append(user_view_history_decoded)

    return result

if __name__ == "__main__" :
    matrix_decoded = decode_matrix(view_history)

    for user_view in matrix_decoded :
        print(user_view)