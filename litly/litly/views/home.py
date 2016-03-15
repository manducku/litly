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
        prev_url = request.POST.get("prev_url")
        resource = Resource.objects.create(
                prev_url= prev_url,
                )

        import hashlib
        m = hashlib.md5()
        next_url = m.hexdigest()[:8]
        resource.next_url = next_url
        resource.save()

        return redirect(
                "home"
                )
        
