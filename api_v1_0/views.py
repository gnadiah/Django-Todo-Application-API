import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Todo_v1_0


@csrf_exempt
def index(request):
    routes = [
        {
            'url': '/api/v1.0/',
            'method': '*',
            'description': 'This is the index page.'
        },
        {
            'url': '/api/v1.0/getTask/',
            'method': 'GET',
            'description': 'Get all tasks.'
        },
        {
            'url': '/api/v1.0/createTask/',
            'method': 'POST',
            'description': 'Create a new task.'
        },
        {
            'url': '/api/v1.0/editTask/<str:task_id>/',
            'method': 'PATCH',
            'description': 'Edit a task.'
        },
        {
            'url': '/api/v1.0/deleteTask/<str:task_id>/',
            'method': 'DELETE',
            'description': 'Delete a task.'
        }
    ]
    return JsonResponse({
        'message': 'Welcome to the Todo API v1.0',
        'routes': routes
    }, status=200)


@csrf_exempt
def get_task(request):
    if request.method != 'GET':
        return JsonResponse({
            "message": "Method not allowed",
        }, status=405)
    else:
        try:
            tasks = Todo_v1_0.objects.all()
        except Exception as e:
            print(e)
            return JsonResponse({
                "message": "Internal Server Error",
            }, status=500)
        task_list = []
        for task in tasks:
            task_list.append({
                "id": task.task_id,
                "title": task.title,
                "content": task.content,
                "created_at": task.created_at,
                "updated_at": task.updated_at,
            })
        if len(task_list) > 0:
            return JsonResponse({
                "message": "Task got successfully",
                "task": task_list,
            }, status=200)
        else:
            return JsonResponse({
                "message": "No task found",
            }, status=404)


@csrf_exempt
def create_task(request):
    if request.method != "POST":
        return JsonResponse({
            "message": "Method not allowed",
        }, status=405)
    else:
        title = request.POST.get("title")
        if title is None:
            return JsonResponse({
                "message": "Title is required",
            }, status=400)
        content = request.POST.get("content")
        if content is None:
            return JsonResponse({
                "message": "Content is required",
            }, status=400)
        try:
            new_task = Todo_v1_0(title=title, content=content)
            new_task.save()
        except Exception as e:
            print(e)
            return JsonResponse({
                "message": "Internal server error",
            }, status=500)
        return JsonResponse({
            "message": "Task created successfully",
            "task": {
                "id": new_task.task_id,
                "title": new_task.title,
                "content": new_task.content,
                "created_at": new_task.created_at,
                "updated_at": new_task.updated_at,
            }
        }, status=201)


@csrf_exempt
def edit_task(request, task_id):
    if request.method != "PATCH":
        return JsonResponse({
            "message": "Method not allowed",
        }, status=405)
    else:
        data = json.loads(request.body)
        try:
            task = Todo_v1_0.objects.get(task_id=task_id)
        except Todo_v1_0.DoesNotExist:
            return JsonResponse({
                "message": "Task not found",
            }, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({
                "message": "Internal server error",
            }, status=500)
        for key in data.keys():
            if hasattr(task, key):
                setattr(task, key, data.get(key))
            else:
                return JsonResponse({
                    "message": "Invalid field",
                }, status=400)
        try:
            task.save()
        except Exception as e:
            print(e)
            return JsonResponse({
                "message": "Internal server error",
            }, status=500)
        return JsonResponse({
            "message": "Task edited successfully",
            "task": {
                "id": task.task_id,
                "title": task.title,
                "content": task.content,
                "created_at": task.created_at,
                "updated_at": task.updated_at,
            }
        }, status=200)


@csrf_exempt
def delete_task(request, task_id):
    if request.method != "DELETE":
        return JsonResponse({
            "message": "Method not allowed",
        }, status=405)
    else:
        try:
            task = Todo_v1_0.objects.get(task_id=task_id)
        except Todo_v1_0.DoesNotExist:
            return JsonResponse({
                "message": "Task not found",
            }, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({
                "message": "Internal server error",
            }, status=500)
        task.delete()
        return JsonResponse({
            "message": "Task deleted successfully",
        }, status=200)
