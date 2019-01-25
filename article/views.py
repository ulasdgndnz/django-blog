from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Article,Comment
from .forms import ArticleForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

#------------------------------------------------------------------------------#
@login_required(login_url="/users/login/")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # 1. Yol
        """
        author = request.user
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")

        newArticle = Article(author=author, title=title, content=content)
        newArticle.save()"""

        # 2. Yol
        article = form.save(commit=False) # commit = False -> newArticle.save()
        # form.save() formda verilenleri yerleştiriyor
        # article = Article(title=title, content=content)
        # biz formda kullanıcıyı göstermediğimiz için kullanıcıyı vermiyor
        # biz onu ayrı olarak kendimiz tanımlıyoruz
        article.author = request.user
        article.save()

        messages.success(request,"Makale Oluşturuldu")
        return redirect('/articles/dashboard/')
    return render(request, 'article/addarticle.html',{"form":form})

@login_required(login_url="/users/login/")
def delete(request, id):
    article = Article.objects.filter(id=id)
    article.delete()
    return redirect("/articles/dashboard/")

@login_required(login_url="/users/login/")
def update(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author != request.user:
        return redirect('/articles/dashboard/')
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        messages.success(request,"Makale Düzenlendi")
        return redirect('/articles/dashboard/')
    return render(request, 'article/update.html', {'form': form})

def detail(request, id):
    keyword = request.GET.get("keyword")
    if keyword:
        article_byTitle = Article.objects.filter(title__icontains = keyword)
        article_byContent = Article.objects.filter(content__icontains = keyword)
        article_list = article_byTitle.union(article_byContent)
        return render(request,'articles.html',{'contacts': article_list})

    article = Article.objects.get(id = id)
    comment = article.comments.all()
    context = {
        "article":article,
        "comment":comment
    }
    return render(request,'article/detail.html', context)

@login_required(login_url="/users/login/")
def dashboard(request):
    article = Article.objects.filter(author=request.user)
    context = {
        "article":article
    }
    return render(request,'article/dashboard.html',context)

def articles(request):
    article_list = Article.objects.all()

    keyword = request.GET.get("keyword")
    if keyword:
        article_byTitle = Article.objects.filter(title__icontains = keyword)
        article_byContent = Article.objects.filter(content__icontains = keyword)
        article_list = article_byTitle.union(article_byContent)
        return render(request,'articles.html',{'articles': article_list})

    paginator = Paginator(article_list, 4) # Show 2 contacts per page
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    context = {
        #"article":Article.objects.all(),
        "users": User.objects.all(),
        'articles': article_list
    }
    return render(request,'articles.html',context)

def addcomment(request,id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
    #return redirect("/articles/detail/" + str(id))
    return redirect(reverse("article:detail",kwargs={"id":id}))
