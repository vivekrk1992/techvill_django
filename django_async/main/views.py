from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import asyncio
from django.http import JsonResponse
from django.views import View
import json


class CheckHealth(APIView):

    def get(self, request):
        return Response(data={"test": "is_working"}, status=status.HTTP_200_OK)


async def send_notification():
    print("Notification start")
    # await time.sleep(5)
    await asyncio.sleep(5)
    print("Notification end")


def save_user():
    time.sleep(1)

class UserApiView(View):

    async def post(self, request):
        data = json.loads(request.body)
        print(data)
        # user save
        save_user()
        print(f"{data['username']} saved successfullly")

        # notification
        # send_notification()
        asyncio.create_task(send_notification())
        print("Notification send successfully")
        return JsonResponse({"test": "is_working"})
