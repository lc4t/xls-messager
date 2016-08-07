from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    if (not request.user.is_active):
        return HttpResponse('not active!')
    if (request.user.is_superuser):
        return HttpResponse('you are admin')
    else:
        return HttpResponse('you are:' + str(request.user.username))


    # return HttpResponse('this is default page')
from django.contrib.auth import authenticate

from asyncmailer.tasks import async_mail
def Send(request):
    async_mail(['lc4t0.0@gmail.com'], # Email (delay no longer required)
      "New Activity on Your Account", # Subject
      context_dict={ # Optional, if supplied, the templated will be rendered before sending
      "message": "Hello! \n Someone gave you a comment today! \n \"%s\"" % 'c.content',
      "button_text": "View",
      "button_url": "hh%sh" % 't.token'
      },
    #   template='email.html', # Optional, you can specify the template for email via this parameter.
                             # If not supplied, a default template will be used.
    #   template_plaintext='email_pt.html' # Optional, the plaintext alternative of template.
      # It is important to note that if you specify the template but not the plaintext template,
      # the default plaintext template will still be used, and vise versa.
    )
    return HttpResponse('success')
