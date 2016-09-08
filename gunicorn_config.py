bind = '0.0.0.0:7777'
backlog = 2048

workers = 4
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

spew= False

daemon = True
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = '/home/siva/toppr_files/tmp'
errorlog = '/home/siva/toppr_files/tmp/error.log'
loglevel = 'info'
accesslog = '/home/siva/toppr_files/tmp/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
proc_name = 'Toppr_Gunicorn'

