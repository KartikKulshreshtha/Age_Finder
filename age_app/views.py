from re import A
from django.shortcuts import render
from datetime import date

def home(request):
    if request.method == "POST":
        Date = request.POST.get('date')
        Month = request.POST.get('month')
        Year = request.POST.get('year')
        
        dob = date(int(Year), int(Month), int(Date))
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        # Age = f'You are {age} years old!!'
        # Age = ' '.join(Age)
        context = {
            'age': age
        }
        return render(request, 'age_app/home.html', context)
    return render(request, 'age_app/home.html')