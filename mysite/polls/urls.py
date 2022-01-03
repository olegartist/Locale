from django.urls import path, include
from .views import IndexViewer, Index

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', IndexViewer.as_view()),
    path('i/', Index),

    #path('i18n/', include('django.conf.urls.i18n')),
    #path('', include('polls/urls')),
]

