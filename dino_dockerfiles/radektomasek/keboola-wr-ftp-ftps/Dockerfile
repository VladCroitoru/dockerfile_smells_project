FROM radektomasek/keboola-base-node-lftp
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

RUN yum update -y nss curl libcurl; yum clean all && git clone https://github.com/radektomasek/keboola-wr-ftp-ftps ./ && npm install

ENTRYPOINT node ./src/index.js --data=/data
