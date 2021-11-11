FROM alpine

MAINTAINER sisidovski <shunya.shishido@gmail.com>

ARG workdir=sync-backend

RUN apk --update add python3 python3-dev
RUN rm -rf /var/cache/apk/*
RUN python3 -m ensurepip
RUN rm -r /usr/lib/python*/ensurepip 
RUN pip3 install --upgrade pip setuptools 
RUN rm -r /root/.cache
RUN pip3 install awscli 
RUN mkdir $workdir

WORKDIR $workdir
ADD /start.sh start.sh

CMD ["/sync-backend/start.sh"]
