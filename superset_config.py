import os
# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 4  # for it to work in heroku basic/hobby dynos increase as you like
SUPERSET_WEBSERVER_PORT = os.environ['PORT']
# ---------------------------------------------------------
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')

# ---------------------------------------------------------
# Flask App Builder configuration
# ---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.environ['SECRET_KEY']

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ['postgres://ddjlvvyrtzwpga:f1601129c10356e5551732ec653b5c33e0630ce42d5a3a8f674f74c1f01cc220@ec2-54-161-208-31.compute-1.amazonaws.com:5432/d5rd9karsicj4i']

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = CSRF_ENABLED = True

# use inserted X-Forwarded-For/X-Forwarded-Proto headers
ENABLE_PROXY_FIX = True
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300
SQLLAB_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300
