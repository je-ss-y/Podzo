from django.shortcuts import render

from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib.auth.models import User


# Create your views here.
from django.http  import HttpResponse

# Create your views here.

# def welcome(request):
#     return render(request, 'welcome.html')

def menu_of_day(request):
   
    menu = Restaurants.todays_menu()
    return render(request, 'all-news/welcome.html', {"menu": menu})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day
@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'menu' in request.GET and request.GET["menu"]:
        search_term = request.GET.get("menu")
        searched_menus = Restaurants.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"menu": searched_menus})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


# def editor(request):
   
#     profile = Editor.editor_profile()
#     # profile = Editor.objects.filter(id=id).first()
#     return render(request, 'all-news/profile.html', {"profile": profile})


def all(request):
   
    profile = Restaurants.todays_menu()
    details = Menu.editor_menu()
    # profile = Editor.objects.filter(id=id).first()
    return render(request, 'all-news/profile.html', {"profile": profile ,"details": details})



# def menu(request):
   
#     details = Menu.editor_menu()
#     # profile = Editor.objects.filter(id=id).first()
#     return render(request, 'all-news/profile.html', {"details": details})



@login_required(login_url='/accounts/login/')
def commenting(request,restaurants_id):
    current_user = request.user
    if request.method == 'POST':
        restauranttocomment = Restaurants.objects.filter(id = restaurants_id).first()
        # user = User.objects.filter(user = current_user.id).first()
        # print(user)
        form =  CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user= current_user
            comment.image =restauranttocomment
            comment.save()
            
        return redirect('menuToday')

    else:
        form = CommentForm()
    return render(request, 'all-news/comment-form.html', {"form": form, 'restaurants_id':restaurants_id})





