FROM python:3.4-onbuild
EXPOSE 8000
CMD [ "gunicorn", "-w", "2", "bookish.wsgi:application", "-b", "0.0.0.0:8000" ]


