from django.contrib import admin
from user.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # user list 사용자명과 비밀번호를 확인할 수 있도록 설정

admin.site.register(User, UserAdmin)