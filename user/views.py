from django.shortcuts import render
from user.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

# URL을 입력하여 페이지를 불러오는 경우 - GET 방식
# 페이지에서 등록 버튼을 눌러서 페이지에 접근하는 경우 - POST 방식
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None) # 템플릿에서 입력한 name 필드에 있는 값을 키값으로 받아옴
        password = request.POST.get('password', None) # 받아온 키값에 값이 없는경우 None값으로 기본값 지정
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        res_data = {} # 응답 메세지를 담을 변수 (dict)

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(username=username, useremail=useremail, password=make_password(password))
            # 데이터베이스에 저장
            user.save()

        # res_data가 html 코드로 전달됨
        return render(request, 'user/register.html', res_data)