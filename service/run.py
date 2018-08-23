from app import app
from app.config import get_env

if __name__ == "__main__":
    app.run(host=get_env('HOST'), port=get_env('PORT'))
