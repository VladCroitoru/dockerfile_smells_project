FROM ubuntu:14.04
MAINTAINER Leon Pegg "leon.pegg@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install software-properties-common -y

RUN add-apt-repository ppa:x2go/stable
RUN apt-add-repository ppa:ubuntu-mate-dev/ppa
RUN apt-add-repository ppa:ubuntu-mate-dev/trusty-mate

RUN apt-get update

RUN apt-get install openssh-server -y
RUN apt-get install ubuntu-mate-core ubuntu-mate-desktop -y
RUN apt-get install x2goserver x2goserver-xsession pwgen -y
RUN apt-get install x2gomatebindings -y

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config

RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

RUN mkdir /var/run/dbus

ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

EXPOSE 22

CMD ["/run.sh"]
