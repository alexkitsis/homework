import asyncio
import os

from celery import Celery

from tasks.processor import Processor

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

processor = Processor()

@celery.task
def create_new():
    asyncio.run(processor.process(10))
    return True

@celery.task
def status(id):
    result = celery.AsyncResult(id)
    return result.status

