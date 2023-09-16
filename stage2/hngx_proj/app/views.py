from django.shortcuts import render
from .models import Person
from .utils import disp
from .serializer import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_all_persons(request):
    try:
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
    except:
        None 

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_person_details(request, query):
    try:
        person = Person.objects.get(name=query)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        person = Person.objects.get(id=query)
        serializer = PersonSerializer(person) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def create_person(request):
    try:
        username = request.data["username"]
        disp(username)
        person = Person.objects.create(name=username)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def update_person(request):
    old_data = request.data["old_data"]
    new_data = request.data["new_data"]
    try:
        person = Person.objects.get(id=old_data)
        person.name = new_data
        person.save()
        return Response({"info": "update successful", "data": PersonSerializer(person).data}, status=status.HTTP_200_OK)
    except:
        person = Person.objects.get(name=old_data)
        person.name = new_data
        person.save()
        return Response({"info": "update successful", "data": PersonSerializer(person).data}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_person(request, query):
    try:
        person = Person.objects.get(id=query)
        disp(PersonSerializer(person).data)
        person.delete()
        return Response({'Success': f"{person.name} deleted successfully"}, status=status.HTTP_200_OK)
    except:
       person = Person.objects.get(name=query)
       PersonSerializer(person).data
       person.delete()
       return Response({'Success': f"{person.name} deleted successfully"}, status=status.HTTP_200_OK)
    