from rest_framework.views import Response, APIView


class TestAPI(APIView):
    def get(self, *args, **kwargs):
        return Response({'foo': 'bar'})

    def post(self, *args, **kwargs):
        pass

class TestAPI2(APIView):
    def get(self, *args, **kwargs):
        return Response({'response': 'get result'})

    def post(self, request, *args, **kwars):
        return Response({'response': request.GET.get('response')})
