from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from .models import Book, Borrow, Review, UserProfile, Category
from .forms import UserRegisterForm, DepositForm, ReviewForm
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'library/register.html', {'form': form})

@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            profile = request.user.userprofile
            profile.balance += amount
            profile.save()
            send_mail('Deposit Successful', f'You have deposited {amount} to your account.', 'your_email@gmail.com', [request.user.email])
            messages.success(request, 'Deposit successful')
            return redirect('profile')
    else:
        form = DepositForm()
    return render(request, 'library/deposit.html', {'form': form})

def book_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books, 'categories': categories})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, 'Review submitted successfully')
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'library/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    profile = request.user.userprofile
    if profile.balance >= book.price:
        profile.balance -= book.price
        profile.save()
        Borrow.objects.create(user=request.user, book=book)
        send_mail('Borrow Successful', f'You have borrowed the book "{book.title}".', 'your_email@gmail.com', [request.user.email])
        messages.success(request, 'Book borrowed successfully')
    else:
        messages.error(request, 'Insufficient balance')
    return redirect('book_detail', book_id=book.id)

@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id, user=request.user)
    if not borrow.returned:
        profile = request.user.userprofile
        profile.balance += borrow.book.price
        profile.save()
        borrow.returned = True
        borrow.return_date = timezone.now()
        borrow.save()
        send_mail('Return Successful', f'You have returned the book "{borrow.book.title}".', 'your_email@gmail.com', [request.user.email])
        messages.success(request, 'Book returned successfully')
    return redirect('profile')

@login_required
def profile(request):
    borrows = Borrow.objects.filter(user=request.user)
    return render(request, 'library/profile.html', {'borrows': borrows})
