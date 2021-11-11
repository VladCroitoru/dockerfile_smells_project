FROM python:3.6-alpine

RUN mkdir /service 
WORKDIR /service

ADD ./requirements.txt .
RUN apk add --no-cache gcc musl-dev ; pip install -r requirements.txt

ADD application /service/application
ADD ./cluster.yml /service


ENTRYPOINT ["nameko","run","--config","cluster.yml"]