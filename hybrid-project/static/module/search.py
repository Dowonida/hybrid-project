import requests

Gen={ '드라마':1,  '판타지':2, '서부':3,
 '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9,  '다큐멘터리':10,
 '코미디':11,  '가족':12,
 '미스터리':13, ' 전쟁':14,
 '애니메이션':15,  '범죄':16,
 '뮤지컬':17,  'SF':18,
 '액션':19,  '무협':20,
 '에로':21,  '서스펜스':22,
 '서사':23,  '블랙코미디':24,
 '실험':25,  '영화카툰':26,
 '영화음악':27, ' 영화패러디포스터':28}
# def search(name,genre='드라마'):
#     #헤더 설정
#     request_headers1={'X-Naver-Client-Id': '0F7cODxdTeBb6UNHxJp5','X-Naver-Client-Secret': 'uIhsCGsA0j'}
#     query=name #검색할 내용
#     genre=Gen[genre] #장르 번호
#     URL=f"https://openapi.naver.com/v1/search/movie.json?query={query}&display=10&start=1&genre={genre}" 
    
#     response = requests.get(URL,headers=request_headers1).json()
#     RST=[]
#     for i in response['items']:
#         RST.append(i['title'])
#     RST=i
#     return RST

# print(search('스파이더'))


def search(name,genre=''):
    if not name:#검색어가 없으면
        return [] #아무것도 리턴하지 않아서 search.html에서 검색결과 없음이 나오도록 
    #헤더 설정
    request_headers1={'X-Naver-Client-Id': '0F7cODxdTeBb6UNHxJp5','X-Naver-Client-Secret': 'uIhsCGsA0j'}
    query=name #검색할 내용
    URL=f"https://openapi.naver.com/v1/search/movie.json?query={query}&display=10&start=1" 
    if genre:
        genre=Gen[genre] #장르 번호
        URL+=f'&genre={genre}'
    response = requests.get(URL,headers=request_headers1).json()
    
    #RST=[]
    # for i in response['items']:
    #     RST.append(i)
    # #RST=i
    return response['items']
#a=search('스파이더')['items'][0]
#print(a.keys())
