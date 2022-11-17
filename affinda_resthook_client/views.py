import hashlib
import hmac
import json
from django.shortcuts import render

import requests
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Webhook

api_key = '3087289b75b30a04ccbd3f1f446f88a63f6810d0'
sig_key = b'7ff97f3c1f9a211742903755f3504c778b70f254cbcf5d42cce9612b62023dfe'


def homepage(request):
    webhooks = Webhook.objects.all()
    return render(request, 'homepage.html', {'webhooks': webhooks})


@csrf_exempt
def receiver(request):
    if secret := request.headers.get("X-Hook-Secret"):
        res = requests.post(
            'https://app.affinda.com/v2/resthook_subscriptions/activate',
            headers={
                'Authorization': f'Bearer {api_key}',
                'X-Hook-Secret': secret,
                'Host': 'api.localhost',
            }
        )
        return JsonResponse({'success': 'yay'})  # Confirm subscription intention

    sig_header = request.headers['X-Hook-Signature']
    timestamp, sig_received = sig_header.split('.')
    sig_calculated = hmac.new(sig_key, msg=request.body, digestmod=hashlib.sha256).hexdigest()

    if hmac.compare_digest(sig_received, sig_calculated):
        body = json.loads(request.body)
        Webhook.objects.create(event=body['event'], timestamp=body['timestamp'], payload=json.dumps(body['payload']))
    else:
        Webhook.objects.create(payload='Spies detected!')

    return JsonResponse({'success': 'yay'})
