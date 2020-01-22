from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={
    "message":"welcome my sampletest",
    "players":["勇者","戦士","魔法使い"]         
}
    return render(request,"sampletest/index.html",context)
    # renderは、データとテンプレートを組み合わせて呼び返す、ショートカット関数
    # djangoでは、renderの第三引数にcontextを渡すと、テンプレート側で呼び出すことができる。
