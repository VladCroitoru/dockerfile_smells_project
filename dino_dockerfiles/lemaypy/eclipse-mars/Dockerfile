FROM ubuntu:wily

MAINTAINER Pierre-Yves Lemay <lemaypy@gmail.com>

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/mars/1/eclipse-jee-mars-1-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN apt-get update \
 && apt-get install -y software-properties-common curl \
 \
 && apt-add-repository -y ppa:webupd8team/java \
 && apt-get update \
 && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
 && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
 && apt-get install -y oracle-java8-set-default libgtk2.0-0 libxtst6 \
 \
 && apt-get -y install openssh-server \
 \
 && curl "$DOWNLOAD_URL" | tar vxz -C $INSTALLATION_DIR \
 \
 && apt-get --purge autoremove -y software-properties-common curl \
 && apt-get clean

# Setting openssh
RUN mkdir /var/run/sshd
RUN sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config

RUN adduser --system eclipse
RUN mkdir -p /home/eclipse/.ssh

#test RUN adduser --disabled-password --quiet --gecos '' eclipse
RUN chown -R eclipse:root $INSTALLATION_DIR/eclipse
RUN chmod -R 775 $INSTALLATION_DIR/eclipse

# Setting authorized ssh keys
#pyADD id_rsa.pub /home/eclipse/.ssh/authorized_keys
#pyRUN chmod 400 /home/eclipse/.ssh/authorized_keys && chown eclipse:root /home/eclipse/.ssh/* && chmod 600 /home/eclipse/.ssh/*
# Updating shell to bash
RUN sed -i s#/home/eclipse:/bin/false#/home/eclipse:/bin/bash# /etc/passwd

USER eclipse

EXPOSE 22

#pyCMD ["/usr/sbin/sshd", "-D"]
ENTRYPOINT $INSTALLATION_DIR/eclipse/eclipse
