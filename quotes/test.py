from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from quoteapp.models import Author, Tag, Quote



quotes = Quote.objects.all()

for quote in quotes:
    print (quote)
    break