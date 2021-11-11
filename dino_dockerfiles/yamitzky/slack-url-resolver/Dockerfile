FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["python", "main.py"]
