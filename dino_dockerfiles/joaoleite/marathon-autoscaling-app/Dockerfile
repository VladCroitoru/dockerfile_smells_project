FROM python:3.6-alpine

RUN apk update && apk upgrade && apk add bash git openssh

COPY . /opt/app

RUN pip install -r /opt/app/requirements.txt

CMD ["python", "/opt/app/autoScale/main.py"]