cat setup_mysql_dev.sql | mysql -hlocalhost -uroot
gunicorn --bind 0.0.0.0:5000 api.v1.app:app --daemon
gunicorn --bind 0.0.0.0:5001 front_end.index:app --daemon
