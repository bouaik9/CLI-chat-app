# Chat Application

This is a simple implementation of Celery and RabbitMQ with Django for real-time chat and background task processing.

## Workflow

- Users send messages in chat rooms via WebSockets (using Django Channels).
- Messages are processed and displayed in real time.
- Celery handles background tasks such as message moderation, using RabbitMQ as the message broker.
- Moderated messages are updated in the chat without reloading the page.

![Screenshot from 2025-06-17 11-04-56](https://github.com/user-attachments/assets/b7f9cd67-a429-4f7b-814d-75503525dca2)
![Screenshot from 2025-06-17 11-05-59](https://github.com/user-attachments/assets/d11a7d5e-aa65-4637-abe1-74a54cf9354b)
