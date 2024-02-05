DEBUG = True

USERNAME = "root"
PASSWORD = "admin"

SERVER = "localhost"
DB = "projetoApiFlask"

SQLALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}"