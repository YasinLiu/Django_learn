from django.shortcuts import render


# Create your views here.
def index_test(request):
    return render(request, 'HADCP/index_test.html')
