from django.shortcuts import render,render_to_response,RequestContext
from .models import DescriptionVersion

def return_version(request):
	version = DescriptionVersion.objects.all().first()
	my_context={
	'version':version
	}
	return render_to_response('adminmy/index.html',
                          my_context
                          )
# Create your views here. context_instance=RequestContext(request)
