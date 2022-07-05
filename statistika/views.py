from django.shortcuts import render
from django.views import View
from statistika.models import Statistika


class UyView(View):
    def get(self,request):
        f = Statistika.objects.get()
        return render(request,'index.html',{'foyda':f})
