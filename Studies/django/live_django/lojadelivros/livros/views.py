import json

from .models import Livro
from .serializers import LivrosSerializer

from rest_framework.response import Response
from rest_framework.views import APIView



class LivrosApiView(APIView):
    '''
    Utilize este endereço para gerenciar seus livros.
    '''

    def get(self, request): 
        livros = Livro.objects.all()
        serializer = LivrosSerializer(livros, many=True)
        return Response(serializer.data)

    def post(self, request):      
        return Response(output)

livros_view = LivrosApiView.as_view()