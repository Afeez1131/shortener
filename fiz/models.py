from django.db import models
from .utils import code_generator, create_shortcode

class fizzURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(fizzURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


class fizzURL(models.Model):
    url = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = fizzURLManager()

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        print(self.shortcode)
        super(fizzURL, self).save(*args, **kwargs)