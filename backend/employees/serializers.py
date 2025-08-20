from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    employee_id = serializers.CharField(required=False,max_length=100)
    last_name = serializers.CharField(max_length=100)
    photo = serializers.CharField(required=False,allow_blank=True)
    email = serializers.EmailField()
    designation = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=12, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    