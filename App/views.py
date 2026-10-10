from django.shortcuts import render
from django.core.paginator import Paginator

from App.models import Songs

# Create your views here.
def index(request):
    paginator = Paginator(Songs.objects.all(), 1)  # Show 1 songs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,}
    return render(request, 'index.html', context)