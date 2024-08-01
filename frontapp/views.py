from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')

def attend(request):
    return render(request, 'attend.html')

@login_required
def join_us(request):
    return render(request, 'join_us.html')

# @login_required
# def resources(request):
#     return render(request, 'resources.html')

@login_required
def sponsorship(request):
    return render(request, 'sponsorship.html')


def linkedIn(request):
    return redirect('https://www.linkedin.com/company/attendbrain/')

def contact_us(request):
    return render(request, 'contact_us.html')

@login_required
def dashboard(request):
    posts = Post.objects.all() 
    return render(request, 'dashboard.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
         form = PostForm(request.POST, request.FILES)
         if form.is_valid():
              form.save()
              return redirect('resources')  # Adjust this to your post list view
    else:
         form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
         form = PostForm(request.POST, request.FILES, instance=post)
         if form.is_valid():
              form.save()
              return redirect('resources')
    else:
            form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('dashboard')
    

def resources(request):
   posts = Post.objects.all()
   return render(request, 'resources.html', {'posts': posts})

def resource_view(request, slug):
   post = get_object_or_404(Post, slug=slug)
   return render(request, 'resource_view.html', {'post': post})