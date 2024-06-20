from django.shortcuts import render
from .models import user
from .forms import UserProfile
from django.shortcuts import get_object_or_404
# Create your views here.
def user(request):
    return render(request, 'user.html')
