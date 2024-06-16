from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.
from TaskManagement.models import Task, Users



@csrf_exempt
def update_task(request, user_id, task_id):
    if request.method == "PUT":
        print("Get Inside")
        data = json.loads(request.body)
        try:    
            task_exist = get_object_or_404(Task, user_id=user_id, id = task_id)
        
            update = Task.objects.filter(user_id=user_id, id=task_id).update(status = data['status'])
            return JsonResponse({"msg" : "Updated Successfully"})
        except Exception:
            return JsonResponse({"msg" : "No user_id found"})
    elif request.method == "GET":
        print("Retrieve Data")
        try:
            task_exist = get_object_or_404(Task, user_id=user_id, id = task_id)
            print(task_exist)
            detail = {
                'id' : task_exist.id,
                'title': task_exist.title,
                'description': task_exist.description,
                'due_date': task_exist.due_date,
                'status': task_exist.status,
                'user_id': task_exist.user_id
            }
            return JsonResponse(detail)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == "DELETE":
        try:
            task_exist = get_object_or_404(Task, user_id=user_id, id = task_id)
            task_exist.delete()
            return JsonResponse({'msg' : 'Task Deleted Successfully'})
        except:
            return JsonResponse({'msg':"No Task Found"})







@csrf_exempt
def create_task(request, user_id):
    print(user_id)
    print("Yes")
    if request.method == 'POST':
        print("Inside")
        data = json.loads(request.body)
        print(data)
        print(data['title'])
        title = data['title']
        description = data['description']
        due_date = data['due_date']
        status = data['status']

        
        try:
            task_exists = Task.objects.filter(title=title, user_id=user_id).exists()

            if task_exists == True:
                return JsonResponse({"msg": "Task Already assigned"})
            user = Task.objects.create(title=title, description=description, due_date=due_date,status=status, user_id=user_id)
            user.save()
            print(title, description, due_date, status)
            return JsonResponse({'msg':"Task Assigned", 'task_id' :  user.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == "GET":

        try:
            user_id_exists = Task.objects.filter(user_id=user_id)
            check = user_id_exists.exists()
            if check == True:
                task_list = list(user_id_exists.values())
                print("Details : ", task_list)
                details = {}
                for i in range(len(task_list)):
                    details[i] = task_list[i]

                #task_list = list(details.values())
                return JsonResponse(details)
            else:
                return JsonResponse({'msg' : "User_id not found"})  
        except:
            return JsonResponse({'msg' : "User_id not found"})        
        
@csrf_exempt        
def create_user(request):
    if request.method == 'POST':
        print("Inside")
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
    try:
        user = Users.objects.create(name = name, email = email)
        print(user)
        return JsonResponse({'id':user.user_id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


