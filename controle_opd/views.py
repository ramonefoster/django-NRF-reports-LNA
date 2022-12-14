from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import ListView
from .models import DispModel, ReportModel
from django.core.paginator import Paginator

# Create your views here.
class IndexView(ListView):
    template_name = 'controle_opd/index.html'
    model = ReportModel
    ordering = ["-horario"]
    context_object_name = "records"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset
        return data

class SingleAddr(ListView):
    template_name = 'controle_opd/index.html'
    model = ReportModel
    ordering = ["-horario"]
    context_object_name = "records"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('slug'):
            queryset = queryset.filter(addr__addr__contains=self.kwargs['slug'])
        data = queryset
        return data

# class SingleAddr(View):
#     def get(self, request, slug):
#         reports = ReportModel.objects.filter(addr__addr__contains=slug).order_by("-horario")
#         disp = DispModel.objects.get(addr__contains=slug)

#         paginator = Paginator(reports, 10)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         if paginator.num_pages > 1:
#             is_paginated = True
#         else:
#             is_paginated = False

#         return render(request, 'controle_opd/single-addr.html', {
#             "records": reports,
#             "disp": disp,
#             "page_obj": page_obj,
#             "is_paginated": is_paginated,
#             "paginator": paginator
#         })