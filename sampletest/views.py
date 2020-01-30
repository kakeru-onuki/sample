from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
def index(request):
    articles=Article.objects.all()
    context={
    "message":"welcome my sampletest",
    "players":["勇者","戦士","魔法使い"],
    "articles": articles,
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

def create(request):
    article=Article(content="Hello sampletestooooo",user_name="PAIZADAZE☆")
    article.save()
    articles=Article.objects.all()
    context={
    "message":"Create article",
    "articles": articles,
}
    return render(request,"sampletest/index.html",context)

def delete(request,id):
    article = get_object_or_404(Article,pk=id)
    article.delete()

    articles="Article.objects.all()"
    context={
    "message":"Delete Article"+str(id),
    "article":article,
    }
    return render(request,"sampletest/detail.html",context)
