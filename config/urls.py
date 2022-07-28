from django.contrib import admin
from django.urls import path
from mahsulotlar.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name = 'home'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('items/',MahsulotlarView.as_view(),name = 'mahsulotlar'),
    path('qarzlar/',QarzlarView.as_view(),name = 'qarzlar'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("hisob/", HisobotView.as_view(), name="hisobot"),
    path("add_item/", MahsulotQoshView.as_view(), name="add_item"),
    path("add_info/", MalumotQoshView.as_view(), name="add_info"),
    path('stat/',UyView.as_view(),name = 'house'),
    path('cart/',ShopCartView.as_view(),name = 'cart'),
]
