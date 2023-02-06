from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.core.paginator import Paginator
from .serializers import ClientSerializer
from .models import Client
from .paginations import PageNumberPagination

ValidationError.status_code = 422


# Tem duas formas de fazer a mesma api usando o mesmo serializer, como ViewSet e muito roubado eu fiz como funçao tambem


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoints made a little too easy.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'cpf'
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def client_list(request):
    """
    List all clients, or create a new one.
    """
    if request.method == 'GET':
        page_size = int(request.GET.get('page_size')) or 10
        clients = Client.objects.all()
        paginator = Paginator(clients, page_size)
        page_number = int(request.GET.get('page')) or 1
        clients_page = paginator.get_page(page_number)
        serializer = ClientSerializer(clients_page, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    """
    Retrieve, update or delete a client.
    """
    try:
        if len(str(pk)) == 11:
            client = Client.objects.get(cpf=pk)
        else:
            client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
