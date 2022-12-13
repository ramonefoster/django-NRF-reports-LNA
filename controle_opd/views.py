from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import ListView
from .models import DispModel, ReportModel

# Create your views here.
class IndexView(ListView):
    template_name = 'controle_opd/index.html'
    model = ReportModel
    ordering = ["-horario"]
    context_object_name = "records"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:10]
        return data

class SingleAddr(View):
    def get(self, request, slug):
        reports = ReportModel.objects.filter(addr__addr__contains=slug)
        reports.order_by("-horario")
        disp = DispModel.objects.get(addr__contains=slug)
        return render(request, 'controle_opd/single-addr.html', {
            "records": reports,
            "disp": disp
        })