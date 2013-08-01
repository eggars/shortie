from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import Context, loader
from shorties.models import Record

def index(request):
    if request.method == 'GET':
         return render(request, 'shorties/index.html')
    elif request.method == 'POST':
         rec = Record(url=request.POST['url'])
         rec.save()
         t = loader.get_template('shorties/trim.html')
         c = Context({'enc': rec.to_base64(), 'ref': request.META['HTTP_REFERER']})
         return HttpResponse(t.render(c))
def trimed(request):
    base64_id = request.META['PATH_INFO'].split('/')[-1]
    rec_id = Record.id_from_base64(str(base64_id))
    url = Record.objects.get(pk=rec_id).url
    protocol = 'http://' if len(url.split('://')) == 1 else ''
    return HttpResponsePermanentRedirect(protocol + url)
