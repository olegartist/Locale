from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
#import django.views as View

class IndexViewer(TemplateView):
    template_name = 'polls/templates/index.html'

# class Index(TemplateView):
#     def get(self, request):
#         string = _('Hello world')
#
#         return HttpResponse(string)

def Index(request):
    output = _('StatusPoll Msg')
    string = _('Hello world')
    return HttpResponse(string)






