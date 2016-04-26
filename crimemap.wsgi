#!.venv/bin/python
import sys
sys.path.insert(0, "/var/www/flask-crimemap")
sys.path.insert(0, "/var/www/flask-crimemap/.venv")
from crimemap import app as application
