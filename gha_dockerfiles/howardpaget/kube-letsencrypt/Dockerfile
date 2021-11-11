FROM ubuntu

RUN apt update 
RUN apt install curl -y
RUN apt install certbot -y
# RUN mkdir /etc/letsencrypt

CMD ["/entrypoint.sh"]

COPY secret-patch-template.json /
COPY deployment-patch-template.json /
COPY entrypoint.sh /
