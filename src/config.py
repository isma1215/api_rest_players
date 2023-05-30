from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    MAX_CONTENT_LENGTH = 16*1024*1024

class DevelopmentConfig(Config):
    DEBUG = True

config ={
    'development': DevelopmentConfig
}