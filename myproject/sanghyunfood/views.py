from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json, datetime, requests

from django.http import JsonResponse

def keyboard(request):

        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['급식메뉴']
        })

@csrf_exempt
def message(request):
        message = (request.body).decode('utf-8')
        return_json_str = json.loads(message)
        return_str = return_json_str['content']
        today_date = datetime.date.today().strftime("%m월 %d일")
        req = requests.get('http://www.sanghyun.ms.kr/index.do')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        a_div = soup.find(id="section_6")

        meals = soup.select(
        'p.text_contents > a'
        )
        meal = meals[0].text.replace('\n                           ', '')

        return JsonResponse({
         'message': {
                'text': today_date + '의' + return_str + '입니다.\n' + meal
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['급식메뉴']
                }
         })
