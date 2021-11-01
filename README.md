# Django Celery (Beginners)🎓
This repo is specially made for those, who are beginners for Celery

## 👉🏼 Basic Steps
	- Create Virtual Environment
	- Clone or Download this repository => ( " https://github.com/Shakeel-Nawaz/djcel_001.git " )
	- Download Redis for Windows from https://github.com/tporadowski/redis => ( " https://github.com/tporadowski/redis/releases/download/v5.0.10/Redis-x64-5.0.10.zip " )
	- Extract and Navigate to Redis-x64-5.0.10 folder & use redis-server.exe to start Redis Server (For BASH in Windows => """ $ ./redis-server.exe redis.windows.conf """)
  - 📣It is recommended to use 3 different Terminals (1: Django Server , 2: Redis Server , 3: Celery Server)
## 👉🏼 Steps after clone
	- Install required packages from requirements.txt => (" pip install requirements.txt ")
	- Execute makemigrations and migrate command
	- Start Redis server 
	- Start django server
	- Start Celery server using """ celery -A djcel_001.celery worker --pool=solo -l info """
	- Comment line 8 from main/views.py & Uncomment line 9,10,11 => save => http://127.0.0.1:8000/ (Takes 20 sec to get response)
	- Uncomment line 8 from main/views.py & Comment line 9,10,11 => save => http://127.0.0.1:8000/ (Takes less than 5 sec to get response)
## Files updated or created list 🧾
- settings.py (line 137 to 146) (UPDATED)📑
	
      CELERY SETTINGS

      CEL_BROKER_URL = "redis://localhost:6379"
      CEL_RESULT_BACKEND = "redis://localhost:6379"
      CEL_ACCEPT_CONTENT = ['application/json']
      CEL_RESULT_SERIALIZER = 'json'
      CEL_TTASK_SERIALIZER = 'json'
      CEL_TIMEZONE = 'Asia/Kolkata'

      CEL_RESULT_BACKEND = 'django-db'
- celery.py (line 1 to 20) (CREATED)📑
    
      import os
      from celery import Celery

      os.environ.setdefault('DJANGO_SETTINGS_MODULE','djcel_001.settings')

      app = Celery('djcel_001')

      app.conf.enable_utc = False

      app.conf.update(timezone = 'Asia/Kolkata')

      app.config_from_object('django.conf:settings',namespace="CEL")

      app.autodiscover_tasks()

      @app.task(bind=True)
      def debug_task(self):
          print('Hai')
          print(f'Request: {self.request!r}')
- __init__.py (line 1 to 3) (UPDATED)📑

      from .celery import app as celery_apa

      __all__ = ('celery_apas',)
- main/tasks.py (line 1 to 17) (CREATED)📑
      
      """

      Note if this file updates or any function in this file is changed

      IT IS MUST TO RESTART THE CELERY SERVER

      """
      from time import sleep
      from celery import shared_task

      @shared_task(bind=True)
      def test_func(self):
          print("Task Started")
          for i in range(10):
              print(i)
              sleep(1)
          return "Task Completed"
- main/views.py (line 1 to 12) (UPDATED)📑

      from time import sleep
      from django.shortcuts import render
      from django.http import HttpResponse
      from main.tasks import test_func

      # Create your views here.
      def home(request):
          test_func.delay()
          # for i in range(20):
          #     print(i)
          #     sleep(1)
          return HttpResponse('Done')
