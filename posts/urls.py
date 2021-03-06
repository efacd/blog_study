"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from posts import views
app_name = 'posts'

urlpatterns = [
    path('list/', views.p_list, name="list"),
    path('create/', views.p_create, name="create"),
    path('<int:post_id>/update/', views.p_update, name="update"),
    path('<int:post_id>/delete/', views.p_delete, name="delete"),
    path('<int:post_id>/detail/', views.p_detail, name="detail"),
]
