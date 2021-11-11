# This dockerfile uses the ubuntu image
# Author: Yale Huang
# Command format: Instruction [arguments / command] ..

# Base image to use, this must be set as the first line
FROM alpine

MAINTAINER Yale Huang <calvino.huang@gmail.com>

# Commands to update the image
RUN apk --no-cache add --update supervisor

RUN apk --no-cache add --virtual .build-dep make gcc g++ && \
  rm -rf /var/cache/apk/* && \
        wget http://siag.nu/pub/pen/pen-0.34.1.tar.gz && \
	tar xvfz pen-0.34.1.tar.gz && \
	cd pen-0.34.1/ && \
	./configure && make && make install && \
	rm -rf /pen-0.34.1.tar.gz /pen-0.34.1 && \
	apk del .build-dep

RUN apk --no-cache add --virtual .wget-dep wget && \
  mkdir -p /opt/kcptun && \
	wget --no-check-certificate -O /root/kcptun-linux-amd64.tar.gz https://github.com/xtaci/kcptun/releases/download/v20200409/kcptun-linux-amd64-20200409.tar.gz && \
	cd /opt/kcptun && \
	tar xvfz /root/kcptun-linux-amd64.tar.gz client_linux_amd64 && \
	rm /root/kcptun-linux-amd64.tar.gz && \
  apk del .wget-dep

COPY balanced_kcp_client /balanced_kcp_client
COPY generate_supervisord_conf /generate_supervisord_conf

ENV SERVER=127.0.0.1 SERVER_PORT=4000 CRYPT=aes KCP_PASSWORD=password MTU=1350 SNDWND=1024 RCVWND=8192 \
	MODE=normal CONN=1 SERVER_COUNT=5 DATASHARD=35 PARITYSHARD=15
EXPOSE 1083/tcp

CMD /balanced_kcp_client
