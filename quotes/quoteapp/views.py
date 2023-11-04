from django.shortcuts import render
from utils.mongodb import get_mongodb



def main(request):
    db = get_mongodb()
    quotes = db.quotes.find()
    return render(request, 'quoteapp/index.html', {"quotes": quotes})
