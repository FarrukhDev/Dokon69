from django.contrib import admin
from statistika.models import Statistika
from django.db.models.aggregates import Sum

@admin.register(Statistika)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("umumiy_foyda","bugungi_savdo")

    def show_average(self, obj):
        result = Statistika.objects.filter(umumiy_foyda=obj).sum(Sum("umumiy_foyda"))
        return result["grade__avg"]
