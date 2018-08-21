import os
from dotenv import load_dotenv

env = os.environ.get('FLASK_ENV')

if env == 'development':
    load_dotenv(dotenv_path='./env/.env.development', verbose=True)
elif env == 'test':
    load_dotenv(dotenv_path='./env/.env.test', verbose=True)

def get_env(key):
    print('tentou pegar')
    print(os.environ.get(key))
    return os.environ.get(key)
