from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse


# Create your views here.
@csrf_exempt
def demo_post(request):
    '''
    @summary: just a demo for HTTP POST API.
    '''
    if request.method == 'POST':
        req = Request(request)
        print req.META.get('CONTENT_TYPE')
        raw_data = req.DATA
        print raw_data
        print raw_data.get('Request')
        return JSONResponse(data=raw_data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP POST method.'},
            status=200)
