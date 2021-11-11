FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python-pip -qq
RUN apt-get install libpq-dev python-dev -qq
RUN apt-get install vim -qq
RUN pip install --upgrade pip -qq
RUN pip install pgcli -qq

ENTRYPOINT ["pgcli"]
