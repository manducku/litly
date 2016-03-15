from django.views.generic import View,TemplateView,CreateView 
from resources.models import Resource 
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

class HomeView(View):
    def get(self, request):
        context = {
                'resources': Resource.objects.all()
                }

        return render(
                request, 
                "home.html",
                context = context,
                )

    def post(self, request):
        Resource.objects.create(
                prev_url = request.POST.get("prev_url")
                )
        return redirect(
                reverse(
                    "home"
                    )
                )

