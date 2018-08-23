from app import app as application
from app.config import get_env

if __name__ == "__main__":
    application.run(host=get_env('HOST'), port=get_env('PORT'))
