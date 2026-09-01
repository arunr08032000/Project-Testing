from django.shortcuts import render

# Create your views here.
def register_employee(request):
    return render(request, 'employees/register.html')