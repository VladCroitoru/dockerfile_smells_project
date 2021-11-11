# syntax=docker/dockerfile:1
FROM --platform=linux/x86-64 python:3
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]