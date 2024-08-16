import numpy as np
from random import randint
import pandas as pd

users = [ "괴벨스","요네프","이사벨라","사이먼","도널드" ]
contents = [ "무한도전","런닝맨","순풍산부인과","거침없이하이킥","9시뉴스","어제경제"]

# 영상 또한 유저를 임베딩하는 과정처럼 피쳐를 따로 정해주지
# 않고 랜덤한 벡터로 초기화 해야하지만 데모 구현을 위해
# comedy, drama, news, economy 총 4개의 장르와 가까운 정도로
# 표현한 벡터로 초기화 
# (영상은 임베딩이 되어 있다고 가정 추후 강의에서 영상또한 임베딩 하는 과정 설명 예정) 
content_vectors = {
    "무한도전" : [0.9,0.25,0.05,0.05],
    "런닝맨" : [ 0.8,0.2,0.05,0.05],
    "순풍산부인과" : [ 0.65, 0.85, 0.02, 0.02 ],
    "거침없이하이킥" : [ 0.7, 0.8, 0.02, 0.01 ],
    "9시뉴스" : [ 0.01, 0.05, 0.95, 0.85  ],
    "어제경제" : [ 0.02, 0.05, 0.85, 0.95 ]
    }

def make_demo_data() :
    # 어느정도 패턴이 존재하는 데모데이터를 만들고
    # 우리가 만든 모델이 이 패턴을 찾아내는지 보기 위해서
    # 유저마다 선호도 점수를 주어 더 큰 확률로 특정 컨텐츠 들이 뽑히도록  유도하기위해
	# 임의적으로 유저마다 선호점수 리스트를 생성

    preference = [ 
        [ 7,5,2,3,1,1], # 괴벨스
        [ 2,4,5,6,7,8], # 요네프
        [ 2,2,8,4,1,2], # 이사벨라
        [ 1,3,2,4,7,9], # 사이먼
        [ 1,1,2,1,9,6], # 도널드
    ]

    def view_content_randomly(user_idx) :
			# 유저의 선호 편향 점수를 가져옵니다.
        additional_point = preference[user_idx]
			# 0부터 20까지의 랜덤한 숫자와 편향 점수를 더해주어
        rullet = list( randint(0,20) + additional_point[content_idx]  for content_idx in range(len(contents)) )
			# 가장 큰 값을 가지는 인덱스를 반환합니다.
        return np.argmax(rullet)

    view_history = [] 

    for _ in range(1000) :
        user_idx = randint(0,len(users)-1)
        content_idx = view_content_randomly(user_idx)
        content_name = contents[content_idx]
        view_history.append((user_idx,users[user_idx],content_idx,content_name))

    df = pd.DataFrame(view_history,columns=["user_index","user_name","content_idx","content_name"])
    return df

def get_user_ratings(df_interaction) :
	# user_index와 content_idx가 같은 값인 행들의 개수를 저장합니다.
    df_user_view_count = df_interaction.groupby(["user_index","content_idx"]).count()["content_name"]
    print(df_user_view_count)
    ratings = []

    for idx in range(len(users)) :
        views = df_user_view_count[idx].values

        total_view = sum(views)
        rating = views / total_view

        ratings.append(rating)

    return ratings

def init_user_vectors(user_num,feature_num) :

    user_vectors = []

    for i in range(user_num) :
        user_v = np.random.normal(size=feature_num)
        user_vectors.append(user_v)

    return user_vectors

def update(user_vector,content_vector,loss,step_size=0.01) :

    for idx in range(len(user_vector)) :
        yn = content_vector[idx]
				
		# loss와 step_size에 비례해 기존 가중치를 조정합니다.
        dxn = (loss*step_size) * yn

        user_vector[idx] += dxn

if __name__ == "__main__" :
	# 데모 데이터 생성
    df = make_demo_data()
	# 4개의 피쳐를 가지는 5명의 유저를 벡터를 생성
    user_vectors = init_user_vectors(5,4)
    content_vector_list = list( content_vectors[x] for x in content_vectors )

    ratings = get_user_ratings(df)

    def batch() :
        loss_total = 0

        for user_index in range(len(users)) :
            for cidx,cv in enumerate(content_vectors) :
                rating_real = ratings[user_index][cidx] 

                cv = content_vectors[cv]

                v = np.dot(user_vectors[user_index],cv)

                loss = rating_real - v

                update(user_vectors[user_index],cv,loss)

            loss_total += loss

        return loss_total

    def train() :
        i = 0
        loss_history = []

        while i < 1000 :
            loss_total = batch()

            if i % 10 == 0 :
                print(f"{i} batch - loss : {loss_total}")

            i += 1
            loss_history.append(loss_total)

        return loss_history

    history = train()
    donald_vector = user_vectors[-1]
    print(donald_vector)
