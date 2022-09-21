from contextlib import redirect_stderr
import imp
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from books.models  import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def index(request) :
    books=Book.objects.all()
    return render (request, 'books/index.html', {'Books':books})

@login_required
def details(request, id) :
    books=Book.objects.get(id=id)
    print(books)
    return render (request, 'books/details.html', {'books':books})

@login_required
def create (request) :
    if request.POST :
        new_book= Book(title=request.POST['title'],author=request.POST['author'],price=request.POST['price'])
        new_book.save()
        return redirect('/books')
    return render(request, 'books/create.html')

@login_required
def update(request, id) :
    books=Book.objects.get(id=id)
    if request.POST :
        new_book= Book(title=request.POST['title'],author=request.POST['author'],price=request.POST['price'])
        new_book.save()
        books.delete()
        return redirect('/books')
    return render (request, 'books/update.html', {'books':books})

@login_required
def delete(request, id) :
    books=Book.objects.get(id=id)
    books.delete()
    return redirect('/books/')

def signup(request) :
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    form=UserCreationForm()
    return render(request, 'registration/signup.html', {'form' : form})
