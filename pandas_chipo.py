from google.colab import files

uploaded = files.upload()

import pandas as pd
import io

chipo = pd.read_csv(io.BytesIO(uploaded['chipotle.tsv']),sep='\t')

#shape은 데이터프레임의 행과 열의 크기를 제공

print(chipo.shape)

#info()는 데이터프레임의 행과 열의 구성정보를 제공한다.

print(chipo.info())

print(chipo.columns)

print(chipo.index)

#딕셔너리 구조 만들기
dict_data ={'a':1,'b':2,'c':3,'d':4}

#판다스 Series()함수로 딕셔너리를 시리즈로 변환

sr = pd.Series(dict_data)

print(type(sr))
print(sr)

#리스트 구조 만들기

list_data =['2019-12-02',3.14,'ABC',100,True]

#판다스 Series()함수로 리스트를 시리즈로 변환

sr=pd.Series(list_data)
print(type(sr))
print(sr)

#열이름 : key, value로 리스트 갖는 딕셔너리 정의
dict_data  ={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12]}

#판다스 DataFrame()함수로 딕셔너리를 데이터프레임으로 전환

df = pd.DataFrame(dict_data)

print(type(df))
print(df)

#요소의 개수가 같은 3개의 리스트 만들기
names =['Bob',"hessica",'mary']
birth =['73','1212','813']
custom = [1,5,3]

#zip()함수를 통해 요소 묶기

BabyDataSet = list(zip(names,birth,custom))
df = pd.DataFrame(data =BabyDataSet,columns=['names','birth','custom'])

#head()함수를 통해 상위 5개만 출력

df.head()


#order_id는 숫자의 의미를 가지지 않기 때문에 astype를 통해 형변환을 해준다.

chipo['order_id'] = chipo['order_id'].astype(str)

#describe를 통해 기초 통계량을 확인한다.

print(chipo.describe())

#unique로 범주형 피처의 개수 출력하기

print(len(chipo['order_id'].unique()))

print(len(chipo['item_name'].unique()))

#가장 많이 주문한 아이템 Top10

#value_counts()는 각 value가 몇 개 있는지 반환한다. 

item_count = chipo['item_name'].value_counts()[:10] # -> 기본 오름차순
item_count_reverse = chipo['item_name'].value_counts(sort=True, ascending=False)[:10]
print(item_count)
print('-------------------------')
print(item_count_reverse)

#enumerate와 함께 반환해보자

for i, (val,cnt) in enumerate (item_count.items(),1):
  print("Top",i,":",val,cnt) 

#item -> 키, 쌍을 반환


#groupby ->열이름으로 묶어주기

order_count = chipo.groupby('item_name')['order_id'].count() #동일한 아이템 이름으로 묶어주고, 묶인 아이템 이름으로 가진 아이템 아이디가 몇개 있는지  센다.

print(order_count[:10])

chipo.head(10)

item_quantity = chipo.groupby('item_name')['quantity'].sum()

print(item_quantity[:10])

아이템별 주문 총수량을 막대그래프로 시각화한다.

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

#아에팀별 총수량의index를 리스트로 변환한다.
item_name_list = item_quantity.index.tolist()

x_pos= np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos,order_cnt,align='center')

plt.ylabel('orderde_quantity_sum')
plt.title("Distribution of all ordered item")

plt.show()