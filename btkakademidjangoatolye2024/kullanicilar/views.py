from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Comment
from .forms import RegisterForm,CommentForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Kayıt işlemi BAŞARILI : {username}, hoşgeldiniz')
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request,'kullanicilar/register.html',{'form':form})        
         
@login_required
def profilepage(request):
    return render(request,'kullanicilar/profile.html')  

@login_required
def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    comments = profile.comments.all()  

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.profile = profile
            comment.save()
            return redirect('profile_detail', profile_id=profile_id)
    else:
        form = CommentForm()

    return render(request, 'profile_detail.html', {'profile': profile, 'comments': comments, 'form': form})