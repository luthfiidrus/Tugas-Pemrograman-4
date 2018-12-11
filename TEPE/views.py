from django.shortcuts import render
from .models import Comment

# Create your views here.

def box(request):
    context = {} 
    if request.method == "POST" and len(request.POST["komentar"]) != 0 and len(request.POST['penulis']) != 0:
        Comment.objects.create(komen=request.POST["komentar"], penulis=request.POST['penulis'])
    context['comments'] = Comment.objects.all() # comments itu hanyalah suatu variable aja
    return render(request,'TEPE.html', context) # secara otomatis dia nyari di folder templates untuk htmlnya