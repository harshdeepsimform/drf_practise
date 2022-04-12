from django.http import HttpResponse
from datetime import datetime

from .models import IPRecord


class StackOverflowMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs): 
        '''
        record IP address of visitors
        '''
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        get_ip= IPRecord() #imported class from model
        get_ip.ip_address= ipaddress
        get_ip.pub_date = datetime.now() #import datetime
        get_ip.save()

        return None

    def process_request(self, request):
        # request._messages = default_storage(request)
        return None

    def process_exception(self, request, exception): 
        return HttpResponse("in exception")

#RESPONSE FUNCTION:

    # def process_template_response(request, response):
    #     return None

    def process_response(self, request, response):
        """
        Update the storage backend (i.e., save the messages).

        Raise ValueError if not all messages could be stored and DEBUG is True.
        """
        # A higher middleware layer may return a request which does not contain
        # messages storage, so make no assumption that it will be there.
        if hasattr(request, '_messages'):
            unstored_messages = request._messages.update(response)
            # if unstored_messages and settings.DEBUG:
            #     raise ValueError('Not all temporary messages could be stored.')
        return response
