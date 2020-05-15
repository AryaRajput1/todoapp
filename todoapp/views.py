from django.shortcuts import render, redirect
from todoapp.models import Notes, Userdata
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
import re


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            todonote = request.POST.get('note')
            checknote = Notes.objects.filter(
                note=todonote, author=request.user)
            if len(checknote) == 0:
                note = Notes(note=todonote, author=request.user)
                note.save()
                messages.success(request, 'note added in list')

        notes = Notes.objects.filter(author=request.user)
        if len(notes) > 0:
            m = notes
            print(m)
            print('i am here')

        else:
            m = []
            print('notes not exists')

        return render(request, 'index.html', {'notes': m})
    else:
        return redirect('/todo/login/')


def mainnav(request):
    return render(request, 'mainnav.html')


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user19 = authenticate(request, username=name, password=password)
        if user19 is None:
            usersample = User.objects.create_user(name, email, password)
            usersample.save()
            user1 = Userdata(user=usersample, phone=phone)
            user1.save()

            return redirect('/todo/login/')

        else:

            messages.warning(request, 'you are exist')
            return redirect('/todo/login/')
    else:
        messages.warning(
            request, 'if you are new then sign up else goto login')
        return render(request, 'signup.html')


def logins(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user47 = authenticate(request, username=name, password=password)

        if user47 is None:
            return redirect('/todo/signup/')
        else:
            login(request, user47)
            return redirect('/todo/notes/')

    else:

        return render(request, 'login.html')


def deletenotes(request, id):
    Notes.objects.filter(
        note_id=id, author=request.user).update(note_saved=False)
    return redirect('/todo/deleteitems/')


def deleteitems(request):
    if request.user.is_authenticated:
        notes = Notes.objects.filter(author=request.user, note_saved=False)
        if len(notes) > 0:
            m = notes

        else:
            m = []
            print('notes not exists')

        return render(request, 'deleteitems.html', {'notes': m})
    else:
        return redirect('/todo/login/')


def logouts(request):
    logout(request)
    return render(request, 'logout.html')


def cross(request, id):
    Notes.objects.filter(
        note_id=id, author=request.user).update(note_cross=True)
    return redirect('/todo/notes/')


def uncross(request, id):
    Notes.objects.filter(
        note_id=id, author=request.user).update(note_cross=False)
    return redirect('/todo/notes/')


def deleteall(request):
    notes = Notes.objects.filter(author=request.user)
    if len(notes) > 0:
        Notes.objects.filter(author=request.user).update(note_saved=False)
        return redirect('/todo/deleteitems/')
    else:
        return redirect('/todo/notes/')


def restoreall(request):
    notes = Notes.objects.filter(author=request.user)
    if len(notes) > 0:
        Notes.objects.filter(author=request.user).update(
            note_saved=True, note_cross=False)
        return redirect('/todo/notes/')
    else:
        return redirect('/todo/notes/')
def permanentdeleteall(request):
    notes = Notes.objects.filter(author=request.user,note_saved=False)
    if len(notes) > 0:
        notes.delete()
        return redirect('/todo/notes/')
    else:
        return redirect('/todo/deleteitems/')


def restore(request, id):
    Notes.objects.filter(note_id=id, author=request.user).update(
        note_saved=True, note_cross=False)
    return redirect('/todo/notes/')


def permanentdelete(request, id):
    Notes.objects.filter(author=request.user, note_id=id).delete()
    return redirect('/todo/deleteitems/')


def searchnote(request):
   if(request.user.is_authenticated):
    notename=request.GET.get('searchnote')
    print(notename)
    ab=[]
    setnote=Notes.objects.filter(author=request.user,note_saved=True)
    print(setnote)
    for note in setnote:
     print(note)
     m=re.search(notename,note.note)
     if m:
       ab.append(note)
   
    print(ab)
    return render(request, 'search.html', {'notes': ab})
   else:
    return redirect('/todo/notes/')

