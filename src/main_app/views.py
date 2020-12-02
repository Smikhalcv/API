from datetime import datetime
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# import os

from .sheduler_API import Sheduler

# Create your views here.
from django.conf import settings

STATIC_ROOT = settings.STATIC_ROOT


class GetEvents(APIView):
    """Получает данные из файла и выводит их по урлу"""

    def get(self, request):
        file_patch = STATIC_ROOT + "/data_events.json"
        with open(file_patch, encoding="utf-8") as file:
            json_data = json.load(file)

        try:
            end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")
            start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
        except TypeError:
            return Response(
                {
                    "events": json_data,
                    "success": "true",
                },
            )

        events = [
            {
                "id": event["id"],
                "group": event["group"],
                "expert": event["teacher"],
                "lecture": event["lecture"],
                "date": event["date"],
                "time": event["time"],
            }
            for event in json_data
            if (event.get("id") and datetime.strptime(event["date"], "%Y-%m-%d") >= start_date)
            and (datetime.strptime(event["date"], "%Y-%m-%d") <= end_date)
        ]

        return Response(
            {
                "events": events,
                "success": "true",
            },
        )


class GetExperts(APIView):
    """Получает данные из файла и выводит их по урлу"""

    def get(self):
        file_patch = STATIC_ROOT + "/data_experts.json"
        with open(file_patch, encoding="utf-8") as file:
            json_data = json.load(file)

        return Response(
            {
                "experts": json_data,
                "success": "true",
            },
        )


class UpdateEvents(APIView):
    def get(self):
        sheduler = Sheduler()
        events = sheduler.get_all_events()
        file_patch = STATIC_ROOT + "/data_events.json"
        with open(file_patch, "w", encoding="utf-8", newline="\n") as file:
            json.dump(events, file)
        return Response({"success": "true"})


class UpdateExperts(APIView):
    def get(self):
        sheduler = Sheduler()
        experts = sheduler.get_experts()
        file_patch = STATIC_ROOT + "/data_experts.json"
        with open(file_patch, "w", encoding="utf-8", newline="\n") as file:
            json.dump(experts, file)
        return Response({"success": "true"})


class UpdateImages(APIView):
    def get(self):
        sheduler = Sheduler()
        images = sheduler.get_images()
        file_patch = STATIC_ROOT + "/data_images.json"
        with open(file_patch, "w", encoding="utf-8", newline="\n") as file:
            json.dump(images, file)
        return Response({"success": "true"})


class UpdateDefaultEvents(APIView):
    def get(self):
        sheduler = Sheduler()
        images = sheduler.get_default_events()
        file_patch = STATIC_ROOT + "/data_default_lessons.json"
        with open(file_patch, "w", encoding="utf-8", newline="\n") as file:
            json.dump(images, file)
        return Response({"success": "true"})
