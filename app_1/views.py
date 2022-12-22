from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nytimes(request):
    #css-ap8r2t e1ppw5w20
    news_list = []

    try:
        source = requests.get('https://www.nytimes.com/')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')

        all_news = soup.find('div', class_="css-ap8r2t e1ppw5w20").find_all('h3',class_="indicate-hover")

        for news in all_news:
            text = news.text
            # print(text)
            news_list.append(text)

    except Exception as e:
        print(e)

    context = {
        'news_list':news_list
    }

    return render(request, 'nytimes.html', context)


def indiatoday(request):
    news_list = []
    try:
        source = requests.get('https://www.indiatoday.in/')
        source.raise_for_status()  # this will throw an error if url is not found/ wrong

        soup = BeautifulSoup(source.text, 'html.parser')

        all_news = soup.find('div', class_="swiper-wrapper").find_all('h3')
        # print(len(all_news))
        # print(all_news)

        
        for news in all_news:
            text = news.text
            # print(text)
            news_list.append(text)
            
        
    except Exception as e:
        print(e)

    context = {
        'news_list':news_list
    }
    
    return render(request, 'indiatoday.html', context)