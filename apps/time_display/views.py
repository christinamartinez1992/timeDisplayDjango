from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
  # the index function is called when root is visited
def index(request):
	now = timezone.now()
	context = {
		"date" : now.strftime("%b %d, %Y"),
		"time": now.strftime("%I:%M %p")

	}
	return render (request, 'time_display/index.html', context)