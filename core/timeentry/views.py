from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view

# from .decorators import loginRequired

def get_custom_response(success=False, message='something went wrong', data=None, status=400):

    response = {
        'success': success,
        'message': message,
        'data': data
    }
    return Response(response, status=status)

def timestamp():
    return int(datetime.timestamp(datetime.now()))

class CreateTaskView(APIView):

    def get(self,request):
        taskList = Task.objects.all()
        if taskList:
            serializer = TaskSerializer(taskList,many=True)
            custom_response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
            return custom_response
        else:
            error = get_custom_response()
            return error

    def post(self,request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                custom_response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
                return custom_response
            else:
                error = get_custom_response(data=serializer.errors)
                return error


        except Exception as e:
            print(e,'e----------')
            error = get_custom_response()
            return error

@api_view(['POST'])
def tasks_by_date(request):
    try:
        if request.method == POST:
            from_date = request.data.get('from_date')
            to_date = request.data.get('to_date')

            if from_date and to_date:
                
                results = Task.objects.filter(created_at__range=[from_date,to_date])
                if results:
                    serializer = TaskSerializer(results,many=True)
                    custom_response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
                    return custom_response
            else:
                error = get_custom_response()
                return error
        else:
            error = get_custom_response()
            return error

    except Exception:
        response = get_custom_response()
        return response


@api_view(['GET'])
def get_project_fields(request):
    try:
        project_fields = Task.get_projects()
        print(project_fields,'project_fields')
        if project_fields:
            custom_response = get_custom_response(success=True,message="Sucessful",data=project_fields,status=200)
            return custom_response
        else:
            error = get_custom_response(data=serializer.errors)
            return error

    except Exception as e:
        print(e)
        response = get_custom_response()
        return response


class TaskView(APIView):

    def get(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
            if task is None:
                response = get_custom_response()
                return response
            elif Task:
                serializer = TaskSerializer(task)
                custom_response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
                return custom_response
                
        except Exception as e:
            print(e)
            response = get_custom_response()
            return response

    def put(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
            if task is None:
                error = get_custom_response()
                return error

            elif task:
                serializer = TaskSerializer(data=request.data,partial=True)
                if serializer.is_valid():
                    update = serializer.update(instance=task,validated_data=request.data)
                    if update:
                        update.save()
                        custom_response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
                        return custom_response
                else:
                    error = get_custom_response(data=serializer.errors)
                    return error

        except Exception as e:
            response = get_custom_response()
            return response
    
    def delete(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
            if task is None:
                error = get_custom_response()
                return error
            elif task:
                data = task.delete()
                custom_response = get_custom_response(success=True,message="Sucessful",data=data,status=200)
                return custom_response

        except Exception as e:
            response = get_custom_response()
            return response

