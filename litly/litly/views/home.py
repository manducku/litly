from django.views.generic import View,TemplateView,CreateView 
from resources.models import Resource 

class HomeView(TemplateView, CreateView):
    template_name = "home.html"
    fields = ['prev_url', ]

    def get_context_data(self):
        context_data = super(HomeView, self).get_context_data()
        context_data['resources']= Resource.objects.all()

        return context_data


