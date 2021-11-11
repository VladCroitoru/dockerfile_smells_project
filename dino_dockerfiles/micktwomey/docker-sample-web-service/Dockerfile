FROM python:3.4-onbuild

ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD [ "--debug", "--access-logfile", "-", "--error-logfile", "-", "-b", "0.0.0.0:8080", "-b", "0.0.0.0:8081", "web_service:app"]
