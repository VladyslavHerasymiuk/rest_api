from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import Users_Serializer
from .models import Users
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re


# class CreateView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#
#     queryset = Users.objects.all()
#     serializer_class = Users_Serializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles the http GET, PUT and DELETE requests."""
#
#     queryset = Users.objects.all()
#     serializer_class = Users_Serializer

# @csrf_exempt
# def snippet_list(request):
#     """
#        List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#             users = Users.objects.all()
#             serializer = Users_Serializer(users, many=True)
#             return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#             data = JSONParser().parse(request)
#
#             serializer = Users_Serializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         users = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = Users_Serializer(users)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Users_Serializer(users, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         users.delete()
#         return HttpResponse(status=204)

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         users = Users.objects.all()
#         serializer = Users_Serializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = Users_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         users = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = Users_Serializer(users)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = Users_Serializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
class UsersList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = Users_Serializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Users_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Users_Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Users_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetUsers(APIView):

    def post(self, request, format=None):
        items = list(zip(*list(request.data.items())))
        items[0] = list(map(lambda x: re.sub('\s', '', x.strip('+')), items[0]))
        users = Users.objects.raw('SELECT id_user FROM users WHERE number in {}'.format(tuple(items[0])))
        users_id_number = [(i.id_user, i.number) for i in users]
        for i in users_id_number:
                items[0][items[0].index('{}'.format(i[1]))] = i[0]
                #items[0] = [i[0] if val == i[1] else None for val in items[0]]
        items = dict(zip(*items))
        list(map(lambda x: x if type(x) == int else items.pop(x, None),list(items)))
        
        return Response(items)
