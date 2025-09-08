from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406353276',
        'name': 'Inayah Saffanah Asri',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)