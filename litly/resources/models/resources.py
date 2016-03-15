from django.db import models 


class Resource(models.Model):
   prev_url = models.URLField()
   next_url = models.CharField(
           max_length = 50,
           blank = True, 
           null = True,
           )

   create_at = models.DateTimeField(
           auto_now_add=True,
           )
   update_at = models.DateTimeField(
           auto_now=True,
           )

   def __str__(self):
       return self.prev_url
