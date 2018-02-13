from django.shortcuts import render

# Create your views here.

def course_detail(request, slug=None):
	context = {
		"slug": slug,
	}
	return render(request, "course_detail.html", context)

def qc_create(request):
	context = {}
	return render(request,'qc_create.html',context)

def qc_master(request):
	context = {}
	return render(request,'qc_master.html',context)

def qc_update(request, pk=None):
	context = {
		"pk": pk,
	}
	return render(request, "qc_update.html", context)


def question_create(request):
	context = {
	}
	return render(request, "question_create.html", context)