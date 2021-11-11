FROM python:3.6.4-alpine

MAINTAINER Erignoux Laurent <lerignoux@gmail.com>

RUN mkdir /app
WORKDIR /app

ADD ./ /app
RUN pip install -r requirements.txt

CMD ["python", "sub.py"]
