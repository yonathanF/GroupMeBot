from django.shortcuts import render
from twilio.rest import Client

def index(request):
    return render(request, 'polls/index.html')

accountSid = "AC68cadd7f2e0281e30db66d8fc7b7695d";
authToken = "693889b52a7de73338ed51acbf1ac96e";
client = Client(accountSid, authToken);
numbers = ['+17034156746', '+17208082422'];
multiSid = "MG76f8feb0f0545f0838c14863f779134a";

def send(request):
    for i in range(0, len(numbers)):
        client.api.account.messages.create(
        to=numbers[i],
        from_="MG76f8feb0f0545f0838c14863f779134a",
        body="Hello there!")
    return render(request, 'polls/index.html');
