from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def gen_resume(request):
    if request.method == 'POST':
        data = {key: request.POST.get(key, '') for key in request.POST.keys()}
        return render(request, 'resume.html', data)
    return render(request, 'index.html')
