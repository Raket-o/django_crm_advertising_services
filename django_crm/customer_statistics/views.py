from django.shortcuts import render
from django.views.generic.base import View


class CustomerStatistics(View):
    def get(self, request):
        content = {"page": "statistics"}
        return render(request=request,
                      template_name="customer_statistics/statistics.html",
                      context=content)
