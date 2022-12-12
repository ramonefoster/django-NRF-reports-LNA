from django.contrib import admin
from .models import DispModel, ReportModel

# Register your models here.
class DispAdmin(admin.ModelAdmin):
    list_display = ("addr", "nome",)

class ReportAdmin(admin.ModelAdmin):
    list_display = ("addr", )

#Dispositivos
admin.site.register(DispModel, DispAdmin)

#Reports
admin.site.register(ReportModel, ReportAdmin)