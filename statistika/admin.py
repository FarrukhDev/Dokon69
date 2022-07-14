from django.contrib import admin
from statistika.models import Statistika

@admin.register(Statistika)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("umumiy_foyda","bugungi_savdo")

    def show_average(self, obj):
        from django.db.models import Sum
        result = Statistika.objects.filter(umumiy_foyda=obj).sum(Sum("umumiy_foyda"))
        return result["grade__avg"]
