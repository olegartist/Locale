from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

class IndexViewer(TemplateView):
    template_name = 'mysite/templates/index.html'

    def get(self, request, *args, **kwargs):
        print(request.LANGUAGE_CODE)
        #self.object_list = self.get_queryset()
        lnc = request.LANGUAGE_CODE
        context = self.get_context_data()
        context['lnc'] = lnc
        return self.render_to_response(context)

def index(request):
    output = _('Status Msg')
    return HttpResponse(output)






