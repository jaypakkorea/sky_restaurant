from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Restaurant(models.Model):
    province = (('1','Seoul'),('2','Busan'),('3','etc.'))
    region = models.CharField(max_length=20, choices=province)
    name = models.CharField(max_length = 20)
    adress = models.CharField(max_length=50)
    stars = models.IntegerField()
    bestMenu = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mainImage = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

def get_image_filename(instance, filename):
    name = instance.restaurant.name
    slug = slugify(name)
    return "restaurant_images/%s-%s" % (slug, filename)  


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(blank=False, upload_to=get_image_filename)

    image = ProcessedImageField(
    		blank = True,
            upload_to=get_image_filename,
        	processors = [ResizeToFill(350, 520)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    def __str__(self):
       return str(self.restaurant)