FROM debian:sid
RUN apt-get update && apt-get install -y hugo python3 python3-pip
RUN pip3 install pygments
VOLUME /site
WORKDIR /site