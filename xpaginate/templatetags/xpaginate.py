from django import template
from xpaginate.models import *
from django.utils.translation import ugettext as _

register = template.Library()

def xpaginator(parser, token):
    tag_name, page = token.split_contents()
    return RenderXPage(page)

register.tag('xpaginator', xpaginator)