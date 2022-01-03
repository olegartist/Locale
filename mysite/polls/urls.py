from django.urls import path
from .views import IndexViewer, index

urlpatterns = [
    path('', index, name='index'),
    path('', IndexViewer.as_view()),

    #path('i18n/', include('django.conf.urls.i18n')),
    #path('', include('polls/urls')),
]

