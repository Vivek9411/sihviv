from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # for authentication pourpopse
from django.contrib import messages  # flash messages like you have logedin ana logedout
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    # getttig hold of all the records in record table
    records = Record.objects.all

    # check to see if logging in
    if request.method == "POST":
        # do something
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in ')
            return redirect("home")
        else:
            messages.success(request, 'there was an error in login in please try again')
            return redirect("home")
    else:
        return render(request, 'home.html', {})


#
# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "you have been Logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "YOu have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


# create a view for record page
def customer_record(request, pk):
    # cheack if the user reuesting is authenticated
    if request.user.is_authenticated:
        # look up redcords
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to View That Page")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, "Records Deleted Succesfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to to delete records")
        return redirect('home')


def add_records(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                add_records = form.save()
                messages.success(request, 'Records added')
                return redirect('home')
        return render(request, 'add_records.html', {'form': form})
    else:
        messages.success(request, 'you must be logged in to add records')
        return  redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has beeb updated')
            return redirect("home")
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')



