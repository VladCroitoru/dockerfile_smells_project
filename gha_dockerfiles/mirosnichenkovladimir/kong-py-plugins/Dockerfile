FROM kong:2.5.0-ubuntu

LABEL description="Ubuntu + Kong 2.5.0"

USER root

RUN apt update
RUN apt install -y vim python3-pip python3-dev
RUN pip3 install kong-pdk

COPY ./configs/kong.conf /etc/kong/

USER kong
