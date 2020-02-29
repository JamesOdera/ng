from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def album_today(request):
    date = dt.date.today()
    album = Article.todays_album()
    return render(request, 'all-album/today-album.html', {"date": date,"album":album})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_album(request,past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(album_today)

    album = Article.days_album(date)
    return render(request, 'all-album/past-album.html',{"date": date,"album":album})

