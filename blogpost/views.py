from django.shortcuts import render
from .models import Blog
# from .models import Place
# Create your views here.

def read_blog_list(request):
    blogs = Blog.objects.all()
    # places = Place.objects.all()
    return render(request,'blog_list.html',{'blogs':blogs})
    # ,{'places':places}

def blog_new(request):
    return render(request, 'blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.text = request.POST['text']
    blog.date= request.POST['date']
    blog.save()
    blogs = Blog.objects.all()
    return render(request,'blog_list.html',{'blogs':blogs})

# def create_place(request):
#     myplace = Place()
#     myplace.place= request.POST['place']
#     myplace.review= request.POST['review']
#     myplace.save()
#     myplaces= Place.objects.all()
#     return render (request, 'blog_list.html', {'myplaces':myplaces})


def blog_daily(request):
    return render(request, 'blog_daily.html')

    
def blog_beauty(request):
    return render(request, 'blog_beauty.html')

