from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

class IndexViewer(TemplateView):
    template_name = 'polls/templates/index.html'


def index(request):
    output = _('StatusPoll Msg')
    string = _('Hello world')
    return HttpResponse(string)






