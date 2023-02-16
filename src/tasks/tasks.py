import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def send_test_task(self):
    print("Sending sms to number")
