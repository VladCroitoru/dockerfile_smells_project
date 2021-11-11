FROM  resin/armv7hf-debian

# Enable building ARM container on x86 machinery on the web (comment out next line if built on Raspberry)
RUN [ "cross-build-start" ]

ENV SHELL_ROOT_PASSWORD Jeedom123

RUN apt-get clean && apt-get update && apt-get install --no-install-recommends -y wget openssh-server supervisor mysql-client

RUN echo "root:${SHELL_ROOT_PASSWORD}" | chpasswd && \
  sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
  sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

RUN mkdir -p /var/run/sshd /var/log/supervisor
WORKDIR /etc
RUN rm /etc/motd && wget -q https://raw.githubusercontent.com/jeedom/core/master/install/motd 

WORKDIR /etc/supervisor/conf.d
RUN wget -q https://raw.githubusercontent.com/jeedom/core/master/install/OS_specific/Docker/supervisord.conf

WORKDIR /root
RUN rm -f /root/.bashrc && wget -O .bashrc -q https://raw.githubusercontent.com/jeedom/core/master/install/bashrc

RUN wget -O install_docker.sh -q https://raw.githubusercontent.com/jeedom/core/master/install/install.sh && chmod +x /root/install_docker.sh
RUN /root/install_docker.sh -s 2;exit 0
RUN /root/install_docker.sh -s 4;exit 0
RUN /root/install_docker.sh -s 5;exit 0
RUN /root/install_docker.sh -s 7;exit 0
RUN /root/install_docker.sh -s 10;exit 0

RUN wget -q https://raw.githubusercontent.com/jeedom/core/master/install/OS_specific/Docker/init.sh && chmod +x /root/init.sh

CMD ["/root/init.sh"]

# stop processing ARM emulation (comment out next line if built on Raspberry)
RUN [ "cross-build-end" ]
