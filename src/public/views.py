from django.shortcuts import render

# Create your views here.

def course_detail(request, slug=None):
	context = {
		"slug": slug,
	}
	return render(request, "course_detail.html", context)