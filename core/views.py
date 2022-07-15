from django.shortcuts import render
from django.contrib import  messages


from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

from django.conf import settings

api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def userSubscribe(email):
    mailchimp = Client()
    mailchimp.set_config(
        {

            'api_key': api_key,
            'server':server
        }
    )

    member_information = {
        'email_address': email,
        'status': 'subscribed'
    }
    try:
        response = mailchimp.lists.add_list_member(list_id, member_information)
        print(f'{response}')
    except ApiClientError as err:
        print(f'An error occured: {err.text}')

def subscription(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        print(email)
        userSubscribe(email)
        messages.success(request, 'Email received. We will keep in touch')

    return render(request, 'core/index.html')

