FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

RUN yum update -y nss curl libcurl; yum clean all && git clone https://github.com/radektomasek/keboola-wr-sftp-webdav ./ && npm install

ENTRYPOINT node ./src/index.js --data=/data
