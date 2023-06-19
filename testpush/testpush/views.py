from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login

def home(request):
    if not request.user.id:
        login(request, User.objects.first())
    return render(request, 'home.html')

from webpush import send_user_notification, send_group_notification
from webpush.utils import send_to_subscription
from webpush.models import Group, SubscriptionInfo, PushInformation

Group
SubscriptionInfo
PushInformation


def sub_to_group(request):
    group_name = "the_group"
    webpush = {"group": group_name}
    return render(request, 'home.html', {"webpush": webpush})


def send_push_notification(request, username, msg='yo yo yo!'):
    user = request.user
    payload = {"head": "Hi!", "body": msg}
    for user in User.objects.filter(username=username):
        send_user_notification(user=user, payload=payload, ttl=1000)
    return HttpResponse('sent!')
