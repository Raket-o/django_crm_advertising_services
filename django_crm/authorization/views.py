from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import View


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("authorization:login")


