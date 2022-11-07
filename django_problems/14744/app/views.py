from django.shortcuts import render
from .models import Book, Borrowing
from django.http import HttpResponse
from django.contrib.auth.models import User
import json


def get_book_users(request, book_id):
    book = Book.objects.get(pk=book_id)
    borrowings = Borrowing.objects.filter(book=book)
    result = []
    for borrowing in borrowings:
        result.append(
            {'username': str(borrowing.user), 'date': str(borrowing.date)}
        )
    return HttpResponse(json.dumps(result), content_type='application/json')


def borrow_book(request, book_id, user_name):
    book = get_first_or_none(Book.objects.filter(pk=book_id))
    user = get_first_or_none(User.objects.filter(username=user_name))
    if user is None:
        users_borrowings = None
    else:
        users_borrowings = get_first_or_none(
            Book.objects.filter(user_borrowed=user))

    status_code = None
    if book.user_borrowed is not None:
        status_code = 1
    if users_borrowings is not None:
        status_code = 2
    elif (user is None) or (book is None):
        status_code = 3
    else:
        try:
            book.borrow_book(user)
            status_code = 0
        except:
            status_code = 4
    result = {"status": status_code}
    return HttpResponse(json.dumps(result), content_type='application/json')


def return_book(request, book_id):
    book = get_first_or_none(Book.objects.filter(pk=book_id))
    status_code = None

    if book is None:
        status_code = 2
    elif book.user_borrowed is None:
        status_code = 1
    else:
        try:
            book.return_book()
            status_code = 0
        except:
            status_code = 3
    result = {"status": status_code}
    return HttpResponse(json.dumps(result), content_type='application/json')


def get_first_or_none(qs):
    if qs.exists():
        return qs.first()
    return None
