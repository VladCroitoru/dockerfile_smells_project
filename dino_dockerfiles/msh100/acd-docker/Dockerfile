FROM ubuntu:16.04
MAINTAINER Marcus Hughes <hello@msh100.uk>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y encfs python3-pip unionfs-fuse supervisor git cron

RUN pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git

RUN echo "user_allow_other" >> /etc/fuse.conf

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY mount-acd /mount-acd
COPY mount-acd-encfs /mount-acd-encfs
COPY mount-union /mount-union
COPY upload-cron /upload-cron

RUN mkdir /mnt/local-encrypted /mnt/local-decrypted /mnt/acd-encrypted/ /mnt/acd-decrypted/

EXPOSE 22 80
CMD ["/usr/bin/supervisord"]

