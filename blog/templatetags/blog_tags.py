<<<<<<< HEAD
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
=======

from django import template
register=template.Library()
from ..models import Post,Category
from persiantools.jdatetime import  JalaliDateTime 
@register.simple_tag
def test(name):
    return f"Hi {name}"

@register.filter
def upper(value):
    grab = str(value)
    return grab.upper()


@register.filter
def lower(value):
    grab = str(value)
    return grab.lower()

@register.inclusion_tag("blog/includes/blog-recent.html")
def recent_post():
    posts=Post.objects.filter(active=True).order_by("-created_time")[:3]
    return {"posts":posts}



@register.filter
def jalali_date(value):
    return JalaliDateTime(value).strftime("%Y/%m/%d")

@register.inclusion_tag("blog/includes/blog-categories.html")
def categories():
    categories=Category.objects.all()
    posts=Post.objects.filter(active=True)
    categories_count={}
    for cat in categories:
        categories_count[cat]=posts.filter(category__title=cat).count()
    
    return {'categories_count':categories_count}
>>>>>>> New-Session
