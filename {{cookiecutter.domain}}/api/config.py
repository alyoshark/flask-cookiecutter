from os import environ

DEPLOY_ENV = environ.get('DEPLOY', 'test')
if DEPLOY_ENV not in ('dev', 'test', 'prod'):
    DEPLOY_ENV = 'dev'
DEBUG = DEPLOY_ENV != 'prod'

SECRET = '{{cookiecutter.secret}}'
