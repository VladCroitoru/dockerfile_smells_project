FROM mwaeckerlin/ssh
MAINTAINER mwaeckerlin
ENV TERM xterm

ENV BOAR_USER "boar"
ENV BOAR_GROUP "boar"
ENV SSH_PUBKEY ""
ENV BOAR_SOURCE "https://bitbucket.org/mats_ekberg/boar/downloads/boar.16-Nov-2012.tar.gz"
ENV LANG "en_US.UTF-8"

EXPOSE 22

WORKDIR /opt
RUN apt-get update
RUN apt-get -y install python wget mcrypt language-pack-en acl inotify-tools
RUN wget -O- ${BOAR_SOURCE} | tar xz
ADD boar /usr/local/bin/boar
RUN boar mkrepo /boar
RUN setfacl -dm u::rwx /boar
RUN setfacl -dm g::rwx /boar
RUN setfacl -dm o::--- /boar
WORKDIR /boar

ADD start.sh /start.sh
CMD /start.sh

VOLUME /etc/ssh
VOLUME /boar
