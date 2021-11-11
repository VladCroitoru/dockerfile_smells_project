FROM centos:7.2.1511

ENV PATH /opt/node-v6.9.4-linux-x64/bin:$PATH

RUN yum install -y epel-release \
  && yum install -y git

ADD https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.xz /opt

RUN cd /opt \
  && tar -xvf node-v6.9.4-linux-x64.tar.xz \
  && rm -f node-v6.9.4-linux-x64.tar.xz \
  && mkdir /data \
  && git clone https://github.com/seejohnrun/haste-server.git \
  && cd /opt/haste-server \
  && sed -i 's/"redis",/"file", "path": "\/data", /g' config.js \
  && npm install

EXPOSE 7777

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

