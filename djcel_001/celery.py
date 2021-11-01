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
