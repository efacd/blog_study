from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Tag
from posts.forms import PostForm, TagForm

# Create your views here.
def p_list(request):
    post_list = Post.objects.all().order_by('-id')
    return render(request, 'list.html', {'post_list' : post_list})

def p_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        post_form = PostForm()
    return render(request, 'create.html', {'post_form' : post_form})

def p_detail(request, post_id):
    tmp = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # foreign key에 대한 정보가 없어서 에러가 발생했던 것이다
        # tag 객체를 만들어서 foreign 키인 post로 찾은 post 객체를 전달해주고
        # 그 객체를 TagForm의 instance로 추가시켜서 tag_form을 완성하면 에러가 나지 않는다
        tag = Tag(post=tmp)
        tag_form = TagForm(request.POST, instance=tag)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('posts:detail', post_id)
    else:
        tag_form = TagForm()
        context = {
            'post': tmp,
            'tag_form': tag_form
        }
    return render(request, 'detail.html', context)

def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        post_form = PostForm(instance=post)
    return render(request, 'create.html', {'post_form' : post_form})

def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:list')

