# Chat Application

This is a simple implementation of Celery and RabbitMQ with Django for real-time chat and background task processing.

## Workflow

- Users send messages in chat rooms via WebSockets (using Django Channels).
- Messages are processed and displayed in real time.
- Celery handles background tasks such as message moderation, using RabbitMQ as the message broker.
- Moderated messages are updated in the chat without reloading the page.

