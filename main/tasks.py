"""

Note if this file is updates or any function in this file is changed

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