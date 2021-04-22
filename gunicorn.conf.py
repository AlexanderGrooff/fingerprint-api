bind = "0.0.0.0:3000"
workers = 3
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True
loglevel = "debug"
