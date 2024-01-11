from django import forms
import re 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, UserProfile, Comment

from froala_editor.widgets import FroalaEditor

class RegistrationForm(forms.Form):
    last_name = forms.CharField(label='Họ', max_length=30, error_messages={'required': 'Trường này là bắt buộc.'})
    first_name = forms.CharField(label='Tên', max_length=30, error_messages={'required': 'Trường này là bắt buộc.'})
    username = forms.CharField(label='Tài khoản', max_length=40, error_messages={'required': 'Trường này là bắt buộc.'})
    email = forms.EmailField(label='Địa chỉ Email', error_messages={'required': 'Trường này là bắt buộc.'})
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Trường này là bắt buộc.'})
    password2 = forms.CharField(label='Xác nhận mật khẩu', widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Trường này là bắt buộc.'})
    
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Tài Khoản'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Địa Chỉ Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Mật Khẩu'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Xác Nhận Mật Khẩu'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Tên'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Họ'})

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật Khẩu Không Hợp Lệ")

    def clean_username(self):
        #lay username
        username = self.cleaned_data['username']
        # kiem tra cac ki tu deu cac ki thuong trong username
        # them not la ki tu dac biet
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên Tài Khoản có Kí tự Đặc Biệt")
        
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài Khoản đã Tồn tại ")
    
    def save(self):
        # Tạo người dùng
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        # Tạo UserProfile với trường bio
        UserProfile.objects.create(
            user=user,
            bio='',  # Thêm giá trị mặc định hoặc lấy từ form nếu có
            # Thêm các trường khác nếu cần
        )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'toolbarInline': True,
            'content': FroalaEditor(),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age','country','university','city', 'bio','avatar']

    # Add this to handle file input in the form
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'accept': 'image/*'})
    

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit = True):
        comment = super().save(commit = False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ['body']