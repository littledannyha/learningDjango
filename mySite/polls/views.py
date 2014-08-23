from django.shortcuts import render
from django.http import HttpResponse, Http404
from polls.models import Poll
from django.template import RequestContext, loader
from django.shortcuts import render
# Create your views here.

def index(request):
#   bad becaus of hard coding
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	output = ', '.join([p.question for p in latest_poll_list])
# 	return HttpResponse(output)



#   more code than is necessary
#	 latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#	 template = loader.get_template('polls/index.html')
#	 context = RequestContext(request, {
#		 'latest_poll_list': latest_poll_list,
#	 })
#	 return HttpResponse(template.render(context))


#	 shortcut
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
		return HttpResponse("You're voting on poll %s." % poll_id)


