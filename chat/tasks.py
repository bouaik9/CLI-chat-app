from celery import shared_task
from .models import Message

@shared_task
def moderate_message(message_id):
    offensive_words = ['badword1', 'badword2']  # Add offensive words here
    try:
        message = Message.objects.get(id=message_id)
        if any(word in message.content for word in offensive_words):
            message.is_flagged = True
            message.save()
    except Message.DoesNotExist:
        pass