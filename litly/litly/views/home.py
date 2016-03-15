from django.views.generic import View,TemplateView,CreateView 
from resources.models import Resource 
from django.shortcuts import render 
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

        


