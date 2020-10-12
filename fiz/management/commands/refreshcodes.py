from django.core.management.base import BaseCommand, CommandError
from fiz.models import fizzURL
from fiz.utils import create_shortcode

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'



    def handle(self, *args, **options):
        qs = fizzURL.objects.filter(id__gte=1)
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code += 1
        return "{i} New shortcode refreshed".format(i=new_code)

            # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))