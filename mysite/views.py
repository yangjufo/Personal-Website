from django.shortcuts import render
import datetime
from calendar import Calendar


def index(request):
    current_date = datetime.datetime.now()
    current_weekday = datetime.datetime.now().weekday()
    month_iter = Calendar(6).itermonthdates(current_date.year, current_date.month)
    day_before = []
    day_month = []
    day_after = []
    for day in month_iter:
        if day.year < current_date.year or (day.year == current_date.year and day.month < current_date.month):
            day_before.append(day.day)
        elif day.year > current_date.year or (day.year == current_date.year and day.month > current_date.month):
            day_after.append(day.day)
        else:
            day_month.append(day.day)
    return render(request, 'basic/index.html', context={
        'current_date': current_date,
        'current_weekday': current_weekday,
        'day_before': day_before,
        'day_month': day_month,
        'day_after': day_after
    })


def about(request):
    return render(request, 'basic/about.html', context={})
