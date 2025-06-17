# Chat Application

This project is a real-time chat system built using Django, Django Channels, Celery, and RabbitMQ. It allows users to create chat rooms and send messages in real-time.

## Features

- Real-time messaging using WebSockets
- Chat rooms where users can join and communicate
- Message moderation using Celery tasks
- User management and message tracking

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chat
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up RabbitMQ and Redis:
   - Install RabbitMQ and start the service.
   - Install Redis and start the service.

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the chat application at `http://localhost:8000/`.
- Use the admin panel at `http://localhost:8000/admin/` to manage chat rooms and messages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.