FROM python:3.8.6-slim

COPY requirements.txt requirements.txt

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]