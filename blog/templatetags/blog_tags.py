from django import template
from persiantools.jdatetime import JalaliDateTime
from ..models import Post
register = template.Library()


@register.simple_tag
def test(name):
    return f"Hello {name}"


@register.inclusion_tag("blog/includes/blog-recent.html")
def recent_post():
    posts=Post.objects.filter(active=True).order_by("-updated_time")[:4]
    return {"posts":posts}

@register.filter
def lower(value):
    newString=str(value)
    return newString.lower()

@register.filter
def upper(value):
    newString=str(value)
    return newString.upper()

@register.filter
def jalali_date(value):
    return JalaliDateTime(value).strftime("%Y/%m/%d")