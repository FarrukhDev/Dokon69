from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.db.models import Sum
from mahsulotlar.models import Mahsulot, Nasiya
from statistika.models import Statistika


class HomeView(View):
    def get(self,request):
        m  = Mahsulot.objects.all()
        return render(request,'index.html',{'mahsulot':m})
    def post(self,request):
        Mahsulot.objects.create(
            kilosi = request.POST.get('kilosi'),
            blogi = request.POST.get('blogi')
        )
        return redirect('home')

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        a=request.POST.get('ism')
        p=request.POST.get('password')
        u=authenticate(request,username=a,password=p)
        if u is None:
            return redirect('home')
        else:
            login(request,u)
            return redirect('home')

class MahsulotlarView(View):
    def get(self,request):
        m = Mahsulot.objects.all()
        return render(request,'maxsulotlar.html', {'mahsulotlar':m})

class QarzlarView(View):
    def get(self,request):
        n = Nasiya.objects.all()
        return render(request,'qarzlar.html',{'nasiya':n})

class SearchResultsView(ListView):
    model = Mahsulot
    template_name = "maxsulotlar.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Mahsulot.objects.filter(
            Q(nomi__icontains=query) | Q(firma_nomi__icontains=query)
        )
        return object_list

class HisobotView(View):
    def get(self,request):
        m = Mahsulot.objects.all()
        return render(request,'sotuv_hisoboti.html',{'mahsulot':m})

class UyView(View):
    def get(self,request):
        f = Statistika.objects.all()
        a = 0
        for i in f:
           a = i.umumiy_foyda + i.umumiy_foyda
        return render(request,'search_results.html',{'foyda':f},{'umumiy':a})

class MahsulotQoshView(View):
    def get(self,request):
        return render(request,'maxsulot_qoshish.html')
    def post(self,request):
        Mahsulot.objects.create(
            nomi = request.POST.get('nomi'),
            firma_nomi = request.POST.get('firma_nomi'),
            kel_narxi = request.POST.get('kel_narxi'),
            optm_narxi = request.POST.get('optm_narxi'),
            sot_narxi = request.POST.get('sot_narxi'),
            # kel_soni = request.POST.get('kel_soni'),
            # qoldiq = request.POST.get('qoldiq'),
            # foyda = request.POST.get('foyda'),
            # zarar = request.POST.get('zarar'),
        )
        return redirect('home')

class MalumotQoshView(View):
    def get(self, request):
        n = Nasiya.objects.all()
        return render(request, 'malumot_qoshish.html',{'nasiya':n})
    def post(self, request):
        Nasiya.objects.create(
            tovar_nomi = request.POST.get('tovar_nomi'),
            summasi = request.POST.get('summasi'),
            dokon_nomi = request.POST.get('dokon_nomi'),
            xodim_ismi = request.POST.get('xodim_ismi'),
        )
        return redirect('home')

class ShopCartView(View):
    def get(self,request):
        f = Statistika.objects.aggregate(Sum('umumiy_foyda'))
        b = Statistika.objects.aggregate(Sum('bugungi_savdo'))
        return render(request,'Malumot_oldirish.html',{'umumiy':f,'b_savdo':b})

    def post(self,request):
        Statistika.objects.create(
            umumiy_foyda=request.POST.get('umumiy_foyda'),
            bugungi_savdo=request.POST.get('bugungi_savdo'),
        )
        return redirect('cart')



