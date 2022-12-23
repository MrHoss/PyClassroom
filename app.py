from src.routes import app
from src.routes.routes import Routes
Routes()

if __name__ == "__main__":
    app.run(debug=True)