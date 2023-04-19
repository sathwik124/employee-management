from rest_framework import viewsets
from rest_framework.response import Response
from employee_register.models import Employee
from .serializers import RegSerializer
class EmpViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = RegSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer = RegSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def partial_update(self,request,pk):
        queryset = Employee.objects.get(pk=pk)
        serializer = RegSerializer(queryset,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def destroy(self,request,pk):
        queryset = Employee.objects.get(pk=pk)
        queryset.delete()
        return Response({'status':200})
    def retrieve(self,request,pk):
        queryset = Employee.objects.get(pk=pk)
        serializer = RegSerializer(queryset)
        return Response(serializer.data)