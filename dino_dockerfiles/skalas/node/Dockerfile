FROM ubuntu:14.04
MAINTAINER Miguel Escalante <miguel@opi.la>
RUN apt-get update && apt-get install -y build-essential wget  python-dev autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev git  && locale-gen es_MX.UTF-8
## Node installation (0.12.2)
RUN wget http://nodejs.org/dist/v0.12.2/node-v0.12.2.tar.gz -O /tmp/node-v0.12.2.tar.gz && \
tar -xzf /tmp/node-v0.12.2.tar.gz -C /tmp/ && \
cd /tmp/node-v0.12.2/ && \
./configure && \
make && \
make install && \
rm -rf /tmp/*  
EXPOSE 80
