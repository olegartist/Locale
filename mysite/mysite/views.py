from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

class IndexViewer(TemplateView):
    template_name = 'mysite/templates/index.html'

def index(request):
    output = _('Status Msg')
    return HttpResponse(output)






