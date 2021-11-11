FROM python:2-onbuild
EXPOSE 8080
CMD gunicorn -b 0.0.0.0:8080 --access-logfile /dev/stdout --error-logfile /dev/stderr --log-file /dev/stdout katrinbot:app
