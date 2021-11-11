FROM debian:jessie
MAINTAINER Mujtaba Al-Tameemi <mujtaba.altameemi@gmail.com>

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y certbot -t jessie-backports

CMD [ -z "${DOMAINS}" ] && \
    >&2 echo "Please pass DOMAINS environment variable. For more info, go to: hub.docker.com/mujz/lets-encrypt" || \
    certbot certonly --standalone -d $(echo $DOMAINS | sed 's/ /\ -d\ /g')

EXPOSE 80
EXPOSE 443

