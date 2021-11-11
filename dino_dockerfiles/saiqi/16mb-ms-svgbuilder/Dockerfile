FROM python:3.6-alpine

RUN mkdir /service
ADD ./requirements.txt /service
WORKDIR /service
RUN apk add --no-cache gcc musl-dev libxml2-dev libxslt-dev ;\
    pip install -r requirements.txt

ADD application /service/application
ADD ./cluster.yml /service

ENTRYPOINT ["nameko","run","--config","cluster.yml"]