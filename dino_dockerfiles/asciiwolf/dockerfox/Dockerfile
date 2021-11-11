FROM ubuntu:trusty

RUN apt-get update && \
apt-get install -y --force-yes dbus-x11 firefox software-properties-common

RUN apt-add-repository multiverse && apt-get update && \
apt-get install -y flashplugin-installer

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | \
/usr/bin/debconf-set-selections

RUN apt-add-repository ppa:webupd8team/java && apt-get update && \
apt-get install -y --force-yes oracle-java8-installer libxtst6 && \
apt-get clean

CMD /usr/bin/dbus-launch firefox -no-remote -no-xshm
