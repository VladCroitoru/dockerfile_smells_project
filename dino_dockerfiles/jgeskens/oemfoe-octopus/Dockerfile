FROM ubuntu:latest

RUN apt-get update; apt-get install -y python-dev python-pip runit socat
RUN pip install -U pip; pip install -U Django -U six

VOLUME /data/db

ADD . /data/src

WORKDIR /data/src/octopus_admin

RUN mkdir -p /etc/service/octopus_admin
COPY ./runit_run_script /etc/service/octopus_admin/run
RUN chmod +x /etc/service/octopus_admin/run

CMD runsvdir-start
