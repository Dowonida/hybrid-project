from django.shortcuts import render, redirect
from . import models
from .forms import Artform
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

def index(request):
    context={
        'data': models.Art.objects.all(),
    }
    return render(request,'articles/index.html',context)


@login_required #이게 없으면 비로그인 상태에서도 url입력을 통해 write창으로 갈 수가 있다.#알아서 accounts:login으로 리다이렉트된다. 아마도 setting인가에서 계정위치를 account로 했기 때문인듯?
@require_http_methods(['GET','POST'])
def write(request):
    form=Artform(request.POST)
    if request.method=='POST':
        # A=models.Art()
        # a=request.POST.get('title')
        # A.title=a
        if form.is_valid():

            article = form.save()
            article.writer = request.user.username #form.save()의 리턴이 아티클 자체다.
            article.save()
            return redirect('articles:detail', article.pk)
        pass
    else:
        pass
    context={
        'form':form,
    }
    return render(request,'articles/write.html',context)

def detail(request,pk):
    context={
        'data':models.Art.objects.get(pk=pk)
    }
    return render(request, 'articles/detail.html',context)


@require_http_methods(['POST'])
def delete(request,pk):
    if request.user.is_authenticated:
        a=models.Art.objects.get(pk=pk)
        a.delete()
    return redirect('articles:index')

@require_http_methods(['GET','POST'])
def update(request,pk):
    
    article = models.Art.objects.get(pk=pk)

    if request.method == 'POST':#포스트로 왔다는 것은 수정 창에서 제출을 눌렀다는 뜻 
        form = Artform(request.POST, instance=article)
        #request.POST로 수정된 내용을 반영
        #instance=article로 반영할 대상 정함 

        #request.POST를 안넣어주면 계속해서 새 글이 생성된다.
        
        if form.is_valid():
            form.save() #form.save()하면 알아서 수정+저장 
            return redirect('articles:detail', article.pk)
        pass

    else: #다른 메소드로 왔다는 것은 (아직은 GET뿐이지만) 디테일 창에서 '수정'을 눌렀다는 뜻
        form = Artform(instance=article)
        pass

    #여기까지 왔다는 것은 POST가 아닌 메소드로 왔거나, POST인데 valid를 통과 못함->수정창을 보여줘야함
    context={
        'data':article,
        'form':form,

    }
    return render(request, 'articles/update.html',context)







def searching(request):

    a=search(request.GET['search'])   
    for i in range(len(a)):
        a[i]['title']=a[i]['title'].replace('<b>','').replace('</b>','')
    context={
        'data':a,
        'keyword':request.GET['search'],

    }
    return render(request, 'articles/search.html', context)
 

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
def search(name,genre='드라마'):
    #헤더 설정
    request_headers1={'X-Naver-Client-Id': '0F7cODxdTeBb6UNHxJp5','X-Naver-Client-Secret': 'uIhsCGsA0j'}
    query=name #검색할 내용
    genre=Gen[genre] #장르 번호
    URL=f"https://openapi.naver.com/v1/search/movie.json?query={query}&display=10&start=1&genre={genre}" 
    
    response = requests.get(URL,headers=request_headers1).json()
    RST=[]
    for i in response['items']:
        RST.append(i)
    #RST=i
    return RST

#print(search('스파이더'))