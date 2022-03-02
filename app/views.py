from app.models import Todo
from app.serializers import to_do_serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoListAndCreate(APIView):
    def get(self, request):
        query_set = Todo.objects.all()
        serializer = to_do_serializer(query_set, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = to_do_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TodoChangeDelete(APIView):

    def get_objecct(self, pk):
        try:
            return Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            raise NotFound()


    def get(self, request, pk):
        query_set = self.get_objecct(pk)
        serializer = to_do_serializer(query_set)
        return Response(serializer.data)

    def put(self, request, pk):
        query_set = self.get_objecct(pk)
        serializer = to_do_serializer(query_set, data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query_set = self.get_objecct(pk)
        query_set.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

