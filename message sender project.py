import requests
import json


def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization':'K3oLOfh8UFDpmHCxJ07bVnP6RXcayrAjwve1tIgBZQis2WSlEdcjmAnUfSiHGz7BZ8e5KlJCWxhE4TDk',
        'sender_id': 'FSTSMS',
        'message':message,
        'language':'english',
        'route': 'p',
        'numbers':number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


send_sms("7070679294","you get a reward of 100000")
