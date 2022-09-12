장고 깃허브
https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py

현재진도: 112페이지
밑에 password 안내문 수정 또는 지우기
패스워드 변경만들기(이후로직)
닉네임필드 추가하기, hello옆에 username대신 닉네임 나오게만들기


만들기 위한 각 단계별로 꼭해야하는 설정 또는 팁 등을 적을 예정

0. 기본 셋팅
base만들기, 기본적으로 설치해야하는 사항들과 setting에서 해야하는 것

installed app관리나
auth user 등 



1. 게시판 만들기

메소드 관리 등 


2. 계정관리 만들기 


	회원가입페이지 만들기-회원가입은 accounts의 모델에 데이터를 create하는 것과 같음
		urls에 path signup
		views에 def signup에서 회원가입 페이지 연결 기능 넣기
		signup.html에서 회원가입 페이지 만들기
		views의 def signup에서 회원가입페이지로부터 정보 받아서 회원생성 기능 넣기
		회원생성되면 redirect시키기 

		그냥 이대로 진행하면 에러 뜸 이유:
		UserCreationForm이 커스텀 유저모델이 아닌 기존 유저모델로 작성된 클래스이기 때문
		필요한 작업: built in auth forms 변경
		변경대상: '기존' User모델을 참고하는 친구들 -> '새'User 클래스를 모델에 작성했기 때문
			AuthenticationForm, SetPasswordForm, PasswordChangeForm,
			AdminPaswordChangeForm은 대상아님 (User모델을 참조하지 않기 때문)

			UserCreationForm, UserChangeForm은 User를 참조하므로 변경필요
			class Meta: model =User가 등록된 form임
			
			따라서 CustomUserCreationForm을 만들고
			하위 클래스에서 class Meta도 기존의 class Meta를 상속받은 후
			(Meta는 하위 클래스이므로 상위클래스.Meta로 상속)
			model만 get_user_model로 바꿔주면 된다. (get_user_model임포트 필요)


	회원탈퇴 만들기- 회원탈퇴는 accounts의 모델에서 데이터를 delete하는 것과 같음
	로그아웃을 같이 하고 싶으면 반드시 탈퇴 후 로그아웃
	로그아웃을 먼저하면 회원정보가 사라지기 때문 

	회원정보 수정하기- 회원정보수정은 accounts의 모델의 데이터를 update하는 것과 같음
	주의할 점은 form에서 필드를 수정하지 않으면 model의 모든 field가 회원정보수정페이지에 나타나게 됨
	그러면 회원의 등급(권한)과 같은 스스로가 설정하면 안되는 정보까지 접근가능하게 됨
	(그 외에도 최근 로그인 기록, 회원가입날짜처럼 로그를 위한 데이터도 접근가능하게 됨)

	비밀번호 변경하기- 비밀번호 변경하면 세션값이 바껴서 로그인 풀림
			- 안풀리게 하고 싶으면 form.save()다음에
			update_session_auth_hash(request, form.user)를 추가


	request.user.is_authenticated : 로그인 여부를 체크함 등급을 나눠서 체크하지 않음
	html이나 py나 동일	
	이를 이용해서 로그인 한 유저는 로그인이나 회원가입을 못하게
	로그인하지 않은 유저는 글쓰기나 로그아웃을 못하게 할 수 있다.

	로그인한 유저만 사용할 수 있게 하기 위해서 login_required데코레이터를 사용할 수도 있다.
	로그인 이후 어디로 리다이렉트할 것인지 나타난다.
	로그인 이후 리다이렉트를 연결하려면 views의 login함수에 설정을해줘야한다.
	redirect(request.GET.get('next') or 'articles:index') 같은 식으로
	다만 데코레이터는 GET에만 쓰는 것이 좋다. POST에 쓰면 로그인페이지로 간 순간
	POST의 데이터가 다 사라지기 때문 

	html에 POST쓰니까 csrf꼮꼮 넣어라 
3. 기타 명령어
python manage.py createsuperuser