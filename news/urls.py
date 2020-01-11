from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.menu_of_day,name='menuToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/', views.all, name='all'),
    # url(r'^details/', views.menu, name='menu')
    # url(r'^profile/', views.editor, name='editor')
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)