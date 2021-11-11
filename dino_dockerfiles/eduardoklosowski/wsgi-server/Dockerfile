FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN pip install 'gunicorn>=20.0.0,<21'

RUN mkdir /app
WORKDIR /app

COPY wsgi.py ./
RUN python -m compileall .

EXPOSE 8000

CMD ["gunicorn", "wsgi", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
