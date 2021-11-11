FROM python:slim

WORKDIR /app

RUN pip3 install flask gunicorn

ADD src/ .

ENTRYPOINT ["gunicorn", "-c", "config.py", "wsgi:app"]