from django.db import models

# Create your models here.
class User(models.Model):
    # verbose_name은 username, password 대신 출력될 텍스트를 의미
    username = models.CharField(max_length=100, verbose_name='사용자명')
    #useremail = models.EmailField(max_length=100, verbose_name='이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    # auto_now_add로 그 때 시간을 자동으로 입력 가능
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Community_user' # 테이블명 지정
        verbose_name = '커뮤니티 사용자'
        verbose_name_plural = '커뮤니티 사용자'  # 복수형 표현도 설정