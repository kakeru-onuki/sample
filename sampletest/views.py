from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm
# ------------------------------
from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document

def index(request):
    articles=Article.objects.all()
    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():#もしserchFormに正しい値が入ったら
        keyword=searchForm.cleaned_data["keyword"]#keyword1変数にforms.pyのkeywordを代入する。
        articles=Article.objects.filter(content__contains=keyword)
    else:
        searchForm=SearchForm()
        articles=Article.objects.all()
    context={
    "message":"welcome my app",
    "articles": articles,
    "searchForm":searchForm,
}
    return render(request,"sampletest/index.html",context)
    # renderは、データとテンプレートを組み合わせて呼び返す、ショートカット関数
    # djangoでは、renderの第三引数にcontextを渡すと、テンプレート側で呼び出すことができる。
def detail(request,id):
    article = get_object_or_404(Article,pk=id)
    context={
    "message":"Show Article"+str(id),
    "article":article,
    }
    return render(request,"sampletest/detail.html",context)

def new(request):
    articleForm=ArticleForm()

    context={
        "message":"New Article",
        "articleForm":articleForm,
    }
    return render(request,"sampletest/new.html",context)

def create(request):
    if request.method=="POST":
        articleForm=ArticleForm(request.POST)
        if articleForm.is_valid():
            article=articleForm.save()
    context={
    "message":"Create article"+str(article.id),
    "article": article,
}
    return render(request,"sampletest/detail.html",context)

def edit(request,id):
    article = get_object_or_404(Article,pk=id)
    articleForm=ArticleForm(instance=article)
    context={
    "message":"Edit Article"+str(id),
    "article":article,
    "articleForm":articleForm
    }
    return render(request,"sampletest/edit.html",context)

def update(request,id):
    if request.method == "POST":
        article = get_object_or_404(Article,pk=id)
        articleForm=ArticleForm(request.POST , instance=article)
        if articleForm.is_valid():
            articleForm.save()

    context={
    "message":"Edit Article"+str(id),
    "article":article,
    }
    return render(request,"sampletest/detail.html",context)

def delete(request,id):
    article = get_object_or_404(Article,pk=id)
    article.delete()

    articles="Article.objects.all()"
    context={
    "message":"Delete Article"+str(id),
    "article":article,
    }
    return render(request,"sampletest/detail.html",context)

# -------------------
def index1(request):
    if request.method=="POST":
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index1")
    else:
        form =DocumentForm()
        obj=Document.objects.all()

    return render(request,"sampletest/model_form_apload.html",{
        "form":form,
        "obj":obj
    })
