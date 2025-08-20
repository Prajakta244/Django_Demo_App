from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from datetime import datetime
from .serializers import EmployeeSerializer
from .models import Employee
from  demo_proj.db_connection import employees_collection
from demo_proj.helper import get_employee_id

@api_view(['GET'])
def list_employees(request):
    employees = list(employees_collection.find({}, {'_id': 0}))
    serializer = EmployeeSerializer(employees,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        print('data is valid')
        data = serializer.validated_data
        emp_id = get_employee_id()
        data['employee_id'] = f'EMP{emp_id:03d}'
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        result = employees_collection.insert_one(data)
        print("Data inserted:", data)
        data['id'] = str(data.pop('_id'))
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        print('data is invalid')
        return Response({ "success": False, "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_employee(request,id):
    employee = employees_collection.find_one({'employee_id':id})
    if not employee:
        return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
    employee['_id'] = str(employee['_id'])
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

@api_view(['PUT'])
def update_employee(request,id):
    try:
        if not employees_collection.find_one({'employee_id':id}):
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error':'Invalid ID'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['updated_at'] = datetime.utcnow()
        employees_collection.update_one({'employee_id':id},{'$set':data})
        return Response(data)
    return Response({ "success": False, "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request,id):
    try:
        result = employees_collection.delete_many({'first_name':id})
        if result.deleted_count == 0:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({ "errors": "Invalid ID" }, status=status.HTTP_400_BAD_REQUEST)