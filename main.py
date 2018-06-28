from app import create_app, app, db, cli
import cli.app
from app.models import User, Post, Message, Notification, Task
from flask_bootstrap import Bootstrap

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}