from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from static.module.search import search
from . import models
from . import forms

# Create your views here.

def info(request,title):
    a=search(title)[0]
    a['title']=a['title'].replace('<b>','').replace('</b>','')
    context={
        'info':a,
    }


    return render(request, 'movies/info.html', context)

def index(request):
    context = {
        'movies' : models.Movie.objects.all(),
        
    }

    return render(request, 'movies/index.html', context)

def searching(request):
    Genre= request.GET['Genre']
    if Genre=='':
        Genre='전체'

    # if not request.GET['search']:
    #     return render(request, 'movies/search.html', {'genre':Genre})


    a=search(request.GET['search'],request.GET['Genre'])
    #print(a)
    for i in range(len(a)):
        a[i]['title']=a[i]['title'].replace('<b>','').replace('</b>','')
    context={
        'data':a,
        'keyword':request.GET['search'],
        'genre':Genre,

    }
    return render(request, 'movies/search.html', context)
 

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
#         RST.append(i)
#     #RST=i
#     return RST

#print(search('스파이더'))
def create(request):

    form= forms.Movieform(request.POST)
    if request.method=='POST':
        mov = form.save(commit=False)
        mov.user_id=request.user
        mov.save()
        #print(request.user,type(request.user))

        return redirect('movies:index')
    


    context={
        'form':form,
    }

    return render(request,'movies/create.html', context)

def detail(request,movie_pk):
    mov = models.Movie.objects.get(pk=movie_pk)
    comments = mov.comment_set.all()
    commentform = forms.Commentform()
    context={
        'movie':mov,
        'commentform':commentform,
        'comments':comments,
    }
    return render(request,'movies/detail.html',context)

def update(request,movie_pk):
    movie= models.Movie.objects.get(pk=movie_pk)
    user = request.user

    if request.method=='POST':
        if movie.user_id==user:
            pass
 
    if not user.is_authenticated:
        return redirect('accounts:login')
    elif movie.user_id!=user:
        return redirect('movies:detail',movie_pk)
    
    else:

        form=forms.Movieform(instance=movie)
        context={
            'form':form,
            'movie':movie,
        }

        return render(request, 'movies/update.html',context)

def delete(request,movie_pk):
    movie = models.Movie.objects.get(pk=movie_pk)
    print(request.user,movie.user_id,request.user==movie.user_id)
    print(request.method)

    if request.method=='POST' and request.user==movie.user_id:
        movie.delete()
        return redirect('movies:index')
    
    return redirect('movies:detail',movie_pk)
def comments(request,movie_pk):
    com = forms.Commentform(request.POST)
    if com.is_valid():
        if request.user.is_authenticated:
            comment = com.save(commit=False)
            comment.movie_id=models.Movie.objects.get(pk=movie_pk)
            comment.user_id=request.user
            comment.save()

            return redirect('movies:detail',movie_pk)
        else:
            return redirect('accounts:login')


    pass

def comments_delete(request,movie_pk,comment_pk):
    com = models.Comment.objects.get(pk=comment_pk)
    if request.user==com.user_id and request.method=='POST':
        com.delete()
        return redirect('movies:detail',movie_pk)
    return redirect('movies:detail',movie_pk)