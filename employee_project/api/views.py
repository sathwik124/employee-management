from rest_framework.response import Response
from rest_framework.decorators import api_view
from employee_register.models import Employee
from .serializers import RegSerializer
@api_view(['GET'])
def getData(request):
    items = Employee.objects.all()
    serializer = RegSerializer(items,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def addItem(request):
    serializer = RegSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updateItem(request,id):
    obj = Employee.objects.get(id=id)
    serializer = RegSerializer(obj,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteItem(request,id):
    obj = Employee.objects.get(id=id)
    obj.delete()
    return Response({'status':200})
