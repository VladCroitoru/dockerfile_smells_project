FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive
ENV SHELL_ROOT_PASSWORD Mjeedom96
ENV MYSQL_ROOT_PASSWORD mysql123

RUN apt-get update 
RUN  apt-get upgrade -y 
RUN  apt-get dist-upgrade -y 
RUN  apt-get install apt-utils -y 
RUN  apt-get install dialog -y 
RUN  apt-get install wget -y 
RUN  apt-get autoclean -y 
RUN  apt-get install ssh -y

RUN apt-get install supervisor -y

# RUN  apt-get autoremove -y


RUN wget https://raw.githubusercontent.com/jeedom/core/stable/install/install.sh \
	&& chmod +x install.sh \
	&& ./install.sh -m ${MYSQL_ROOT_PASSWORD}


ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get install openssh-server -y

RUN echo "root:${SHELL_ROOT_PASSWORD}" | chpasswd && \
  sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
  sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

RUN mkdir -p /var/run/sshd /var/log/supervisor

ADD init.sh /root/init.sh
RUN chmod +x /root/init.sh
CMD ["/root/init.sh"]

EXPOSE 80
