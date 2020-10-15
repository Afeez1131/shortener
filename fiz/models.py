from django.db import models
from .utils import code_generator, create_shortcode
from .validators import url_validator, dot_com_validator


class fizzURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(fizzURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    # def refresh_codes(self):
    '''
    will get all the url in the models, and create shortcode for them all
    '''
    #     qs = fizzURL.objects.filter(id__gte=1)
    #     new_code = 0
    #     for q in qs:
    #         q.shortcode = create_shortcode(q)
    #         print(q.shortcode)
    #         q.save()
    #         new_code += 1
    #     return "New codes made {i}".format(i=new_code)


class fizzURL(models.Model):
    url = models.CharField(max_length=100, validators=[url_validator, dot_com_validator])
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
        super(fizzURL, self).save(*args, **kwargs)