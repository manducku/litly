from django.views.generic import View
from resources.models import Resource 
from django.shortcuts import redirect

class RedirectionView(View):
    def get(self, request, next_url):
        resource = Resource.objects.get(
                next_url=next_url,
                )

        return redirect(
                resource.prev_url,
                )



