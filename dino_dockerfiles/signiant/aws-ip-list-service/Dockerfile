FROM python:3.7-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /usr/src/app

VOLUME /ip-range-cache

EXPOSE 5000

CMD [ "python", "./aws-ip-list-service.py" ]
