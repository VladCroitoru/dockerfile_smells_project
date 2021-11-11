FROM ubuntu:14.04
MAINTAINER Erik Osterman "e@osterman.com"

ENV DEBIAN_FRONTEND noninteractive

ENV DROPBOX_USER dropbox
ENV DROPBOX_GROUP dropbox
ENV DROPBOX_UID 100
ENV DROPBOX_GID 100

# https://www.dropbox.com/en/help/246

USER root

RUN echo 'deb http://linux.dropbox.com/ubuntu trusty main' > /etc/apt/sources.list.d/dropbox.list && \
    apt-key adv --keyserver pgp.mit.edu --recv-keys 1C61A2656FB57B7E4DE0F4C1FC918B335044912E && \
    apt-get update && \
    apt-get -y install ca-certificates dropbox python-gpgme  && \
    apt-get -qqy autoclean && \
    sed -i 's:/root:/:g' /etc/passwd && \
    echo y | dropbox start -i  && \
    mv /root/.dropbox /root/.dropbox-dist/ /

# Dropbox Lan-sync
EXPOSE 17500

WORKDIR /

ADD dropboxctl /

VOLUME ["/.dropbox", "/Dropbox"]

ENTRYPOINT ["/dropboxctl"]
CMD ["start"]

