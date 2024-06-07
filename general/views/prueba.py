from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config 


class PruebaView(APIView):
    def get(self, request):    
        return Response("Hola mundo")

