import os

class Config:
    # Example: postgresql://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://flaskuser:flaskpass123@localhost/empmgnt_db'  # fallback
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')  # for flash/messages etc.
