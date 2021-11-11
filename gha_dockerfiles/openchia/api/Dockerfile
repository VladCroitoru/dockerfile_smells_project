FROM debian:stable

# Identify the maintainer of an image
LABEL maintainer="contact@openchia.io"

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y

RUN apt-get install python3-virtualenv libpq-dev git vim procps net-tools iputils-ping -y

EXPOSE 8000

WORKDIR /root

COPY ./requirements.txt /root
RUN virtualenv -p python3 venv
RUN ./venv/bin/pip install -r requirements.txt

COPY ./openchiaapi /root/api

COPY ./docker/start.sh /root/

CMD ["bash", "/root/start.sh"]
