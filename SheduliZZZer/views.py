from datetime import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import os

# Create your views here.
from main.settings import STATIC_ROOT, BASE_DIR


class GetData(APIView):
    """Получает данные из файла и выводит их по урлу"""
    def get(self, request):
        file_patch = STATIC_ROOT + '/data_lessons.json'
        with open(file_patch, encoding='utf-8') as file:
            json_data = json.load(file)

        try:
            end_date = datetime.strptime(request.GET.get('end_date'), '%Y-%m-%d')
            start_date = datetime.strptime(request.GET.get('start_date'), '%Y-%m-%d')
        except TypeError:
            return Response({'lessions': json_data, 'success': 'true'})

        lessions = [
            {
                'id': lession['id'],
                'group': lession['group'],
                'teacher': lession['teacher'],
                'lecture': lession['lecture'],
                'date': lession['date'],
                'time': lession['time'],
            }
            for lession in json_data if (lession.get('id') and datetime.strptime(lession['date'], '%Y-%m-%d') >= \
            start_date) and (datetime.strptime(lession['date'], '%Y-%m-%d') <= end_date)]

        return Response({'lessions': lessions, 'success': 'true'}, headers={'Access-Control-Allow-Origin': '*'})