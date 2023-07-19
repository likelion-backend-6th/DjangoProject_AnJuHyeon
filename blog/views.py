from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import EmailPostForm
from .models import Post

def post_list(request):
    post_list = Post.published.all()
    # 페이지당 3개의 게시물로 페이지네이션
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # page_number가 정수가 아닌 경우 첫 번째 페이지 제공
        posts = paginator.page(1)
    except EmptyPage:
        # page_number가 범위를 벗어난 경우 결과의 마지막 페이지 제공
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})
def post_detail(request, year, month, day, post):
    posts = get_object_or_404(post,
                              status=Post.Status.PUBLISHED,
                              slug=post,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
class PostListView(ListView):
    """대체 글 목록 뷰"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # 글 검색을 위해 ID 사용
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    if request.method == 'POST':
        # 폼이 제출되었습니다.
        form = EmailPostForm(request.POST)

        if form.is_valid():
            # 폼 필드가 유효한 경우
            cd = form.cleaned_data
            # ... 이메일 전송
        else:
            form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form})