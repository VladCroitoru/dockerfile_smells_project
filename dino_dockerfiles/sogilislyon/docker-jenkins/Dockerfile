FROM jenkins:latest

USER root
RUN apt-get update && apt-get install -y xvfb

COPY ./xvfb /etc/init.d/xvfb
COPY ./start_xvfb.sh ./start_xvfb.sh

RUN chmod +x ./start_xvfb.sh

RUN ./start_xvfb.sh
