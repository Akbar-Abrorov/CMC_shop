
from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from flask import Response
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
import logging
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__) #playground.views

class HelloView(APIView):
    @method_decorator(cache_page(60 * 5))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('hhtpbin is offline')
        return render(request, 'hello.html', {'name': data})



    #try:
    #send_mail(
    #'Hello, World!',
    #'This is a test email.',
    #'akbar@example.com',
    #['user@bin.com'])
    #except:
    #pass

    #try:
    #mail_admins(
    #'Hello, World!',
    #'This is a test email.',
    #html_message='message'
    #)
    #except:
    #pass

    #try:
    #message = EmailMessage(
    #'Hello, World!',
    #'This is a test email.',
    #'akbar@example.com',
    #['user@bin.com'])
    #message.attach_file('playground/static/images/banana.jpg')
    #message.send()

    #except:
    #pass

    #try:
    #message = BaseEmailMessage(
    #template_name='emails/helli.html',
    #context={
    #'name': 'Akbar'})
    #message.send(['user@bin.com'])

    #except:
    #pass

    #notify_customers.delay('Hello')

