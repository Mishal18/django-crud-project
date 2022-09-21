from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from books.models  import Book

# Create your views here.
def index(request) :
    books=Book.objects.all()
    return render (request, 'books/index.html', {'Books':books})

def details(request, id) :
    books=Book.objects.get(id=id)
    print(books)
    return render (request, 'books/details.html', {'books':books})

def create (request) :
    if request.POST :
        new_book= Book(title=request.POST['title'],author=request.POST['author'],price=request.POST['price'])
        new_book.save()
        return redirect('/books')
    return render(request, 'books/create.html')

def update(request, id) :
    books=Book.objects.get(id=id)
    if request.POST :
        new_book= Book(title=request.POST['title'],author=request.POST['author'],price=request.POST['price'])
        new_book.save()
        books.delete()
        return redirect('/books')
    return render (request, 'books/update.html', {'books':books})

def delete(request, id) :
    books=Book.objects.get(id=id)
    books.delete()
    return redirect('/books/')
