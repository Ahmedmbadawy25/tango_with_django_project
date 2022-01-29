import os

from django import views 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup() 
from rango.models import Category,Page

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories. # This might seem a little bit confusing, but it allows us to iterate 
# through each data structure, and add the data to our models.
    python_pages = [
        {'title': 'Official Python Tutorial',
<<<<<<< HEAD
         'url':'http://docs.python.org/3/tutorial/', 'views':5},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/', 'views':8},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/','views':10}]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views':13},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/', 'views':16},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/', 'views':18} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/', 'views':21},
        {'title':'Flask',
         'url':'http://flask.pocoo.org', 'views':24} ]
=======
         'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'}]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
         'url':'http://flask.pocoo.org'} ]
>>>>>>> d190ee4b4c84f751e4a72bef2f87a85974532ca7

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
<<<<<<< HEAD
            add_page(c, p['title'], p['url'], p['views'])
=======
            add_page(c, p['title'], p['url'])
>>>>>>> d190ee4b4c84f751e4a72bef2f87a85974532ca7

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0] 
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0] 
    c.views = views
    c.likes= likes
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango population script...') 
    populate()