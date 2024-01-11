from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegistrationForm, PostForm,UserProfileForm, CommentForm
from .models import Category, Post, UserProfile, Comment

#thư viện phân trang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

#  tin tức home đóng vai trò như một post list rồi nên thêm vào cái post detail vào 
# recent posts: hiện lên ở chỗ sidebar các bài mới nhất.

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    
    sidebar_posts = Post.objects.exclude(category__name='Tài Liệu').order_by('-date_posted')[:4]
    
    # Pagination
    paginator = Paginator(posts, 5)  # Display 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Pass both posts and sidebar_posts to the template
    return render(request, 'blog/index.html', {'posts': posts, 'sidebar_posts': sidebar_posts})
# post detail 
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, author=request.user, post=post)
        if comment_form.is_valid():
            comment_form.save()
    else:
        comment_form = CommentForm(author=request.user, post=post)
    return render(request, 'blog/post_detail.html', {"post": post, "form": form})

# thao tác thêm post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# thao tác sửa post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# thao tác xóa post
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')

    return render(request, 'blog/post_delete.html', {'post': post})


## --------------------------------------------------------//--------------------------------------------------------##
# thông tin về about
def about(request):
    return render(request,'blog/about.html')

def icpc(request):
    return render(request,'blog/icpc.html')

def olp(request):
    return render(request,'blog/olp.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, 'Đăng Kí Thành Công')
            return redirect("http://127.0.0.1:8000/login/")
        else:
            messages.error(request, 'Đăng Kí Thất Bại')

    context = {'form': form}
    return render(request, 'blog/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('blog-home')

def view_profile(request, username):
    if username is None:
        user_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        user_profile = get_object_or_404(UserProfile, user__username=username)

    user_profile = UserProfile.objects.get(user__username = username)
    
    return render(request, 'blog/view_profile.html', {'profile': user_profile})

# Nội dung của  definition này là bài viết của tôi --> liệt kê các bài viết của mình đã được đăng lên web 
def myPost(request):
    # Assuming 'posts' is a queryset of all posts by the user
    posts = Post.objects.filter(author=request.user)

    # Number of posts to display per page
    posts_per_page = 5
    # Get the current page from the request's GET parameters
    page = request.GET.get('page', 1)
    # Use Django Paginator to paginate the posts
    paginator = Paginator(posts, posts_per_page)
    
    try:
        # Get the specified page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, display the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/mypost.html', context)
     
@login_required
def edit_profile(request):
    user_profile = request.user.userprofile  # Assuming there is a one-to-one relationship between User and UserProfile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('view_profile', username=request.user.username)
        else:
            messages.error(request, 'Error updating profile. Please correct the errors below.')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'blog/edit_profile.html', {'form': form})

# Thay đổi mật khẩu 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Cập nhật session auth để tránh đăng xuất
            messages.success(request, 'Mật khẩu đã được thay đổi thành công.')
            return redirect('view_profile', username=request.user.username)
        else:
            messages.error(request, 'Vui lòng sửa các lỗi bên dưới.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blog/change_password.html', {'form': form})