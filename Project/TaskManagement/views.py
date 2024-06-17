from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.
from TaskManagement.models import Task, Users

from django.forms.models import model_to_dict




@csrf_exempt
def update_task(request, user_id, task_id):
    if request.method == "PUT":
        data = json.loads(request.body)

        try:    
            Task.objects.filter(user_id=user_id, id=task_id).update(status = data['status'])
            return JsonResponse({"status" : 1})
        except Exception:
            return JsonResponse({"status" : 0, "msg" : "No user_id found"})
        
    elif request.method == "GET":
        try:
            task = get_object_or_404(Task, user_id=user_id, id = task_id)

            details = {
                'id' : task.id,
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date,
                'status': task.status,
                'user_id': task.user_id
            }
            return JsonResponse({"status" : 1, "data" : details})
        except Exception as e:
            return JsonResponse({"status" : 0, "msg" :  str(e)})
    
    elif request.method == "DELETE":
        try:
            task = get_object_or_404(Task, user_id=user_id, id = task_id)
            task.delete()
            return JsonResponse({"status" : 1})
        except Exception as e:
            return JsonResponse({"status" : 0, "msg" :  str(e)})



@csrf_exempt
def task_creation_updation(request, user_id):

    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        description = data['description']
        due_date = data['due_date']

        
        try:
            user = Task.objects.create(title=title, description=description, due_date=due_date, user_id=user_id)
            user.save()
            return JsonResponse({"status" : 1, "task_id" :  user.id})
        except Exception as e:
            return JsonResponse({"status" : 0, "msg": str(e)})
        
    elif request.method == "GET":
        try:
            user_id = Task.objects.filter(user_id=user_id)
            arr = [model_to_dict(i) for i in user_id]
            
            if len(arr) >= 1:
                return JsonResponse({"status" : 1, "data" : arr})
            else:
                return JsonResponse({"status" : 0, 'msg' : "User_id not found"})  
        except Exception as e:
            return JsonResponse({"status" : 0, "msg" : str(e)})        
        
@csrf_exempt        
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        try:
            user = Users.objects.create(name = name, email = email)
            return JsonResponse({"status" : 1, "id" : user.user_id})

        except Exception as e:
            return JsonResponse({"status" : 0, 'msg': str(e)})


