from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from TaskManagement.models import Task, Users

@csrf_exempt
def update_task(request, user_id, task_id):
    if request.method == "PUT":
        print("Get Inside")
        data = json.loads(request.body)
        task_exist = Task.objects.filter(user_id=user_id, id=task_id).exists()
        if task_exist == True:
            update = Task.objects.filter(user_id=user_id, id=task_id).update(status = data['status'])
            return JsonResponse({"msg" : update})
        else:
            return JsonResponse({"msg" : "No user_id found"})


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
        task_exists = Task.objects.filter(title=title, user_id=user_id).exists()
        print(task_exists)
        if task_exists == True:
            return JsonResponse({"msg": "Task Already assigned"})
        try:
            user = Task.objects.create(title=title, description=description, due_date=due_date,status=status, user_id=user_id)
            user.save()
            print(title, description, due_date, status)
            return JsonResponse({'msg':"Task Assigned", 'task_id' :  user.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == "GET":
        user_id_exists = Task.objects.filter(user_id=user_id)
        check = user_id_exists.exists()
        print(Task.objects.all())
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


