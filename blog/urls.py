from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    #view chính 
    path('',views.home , name = "blog-home"),

    path('about/', views.about , name = "blog-about"),
    #path for ICPC information
    path('icpc/', views.icpc, name = "blog-icpc"),
    #Path for OLP Information 
    path('olp/', views.olp, name = "blog-olp"),


    #path for register
    path('register/',views.register, name="blog-register"),
    #path for My Post (Bài viết của tôi )
    path('mypost/',views.myPost, name= "blog-mypost"),

    path('login/', LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('logout/', views.logout_user, name="logout"),

# các thao tác như CRUD (Create, Read, Update, Delete)
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    
    path('view_profile/<str:username>/', views.view_profile, name='view_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
    # path thay đổi mật khẩu
    path('change-password/', views.change_password, name='change_password'),
]

from django.conf import settings
from django.conf.urls.static import static

# Phục vụ các tập tin media trong quá trình làm web

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)