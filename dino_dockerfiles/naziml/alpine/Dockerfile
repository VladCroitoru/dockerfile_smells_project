FROM alpine:latest

COPY content /usr/share/nginx/html
COPY startup /opt/startup

RUN  echo "root:Docker!" | chpasswd && \
     apk update && \
     apk add --update openssl nginx openssh-server vim curl wget tcptraceroute && \
     chmod 755 /opt/startup/init_container.sh 

COPY sshd_config /etc/ssh/
COPY etc/nginx.conf /etc/nginx/nginx.conf
COPY etc/common.conf /etc/nginx/common.conf
COPY etc/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY etc/conf.d/ssl.conf /etc/nginx/conf.d/ssl.conf

EXPOSE 2222 80
ENTRYPOINT ["/opt/startup/init_container.sh"]

