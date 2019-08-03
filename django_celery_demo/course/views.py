from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from course.tasks import CourseTask

def do(request):
    print ("start do request")
    # 此处不需要再实例化 通过元类创建 <class 'celery.app.task.TaskType'>
    # CourseTask.delay()
    CourseTask.apply_async(args=("hello",),queue="beat_tasks")
    print ("end do request")
    return JsonResponse(dict(result="OK"))