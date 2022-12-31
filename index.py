from src.routes import app
from src.database.models import user_datastore
from src.routes.routes import Routes,inject_user
from flask_security import Security
Routes()

app.template_context_processors[None].append(inject_user)
app.secret_key = "super secret key"
Security(app, user_datastore)

if __name__ == "__main__":
    app.run(debug=True)