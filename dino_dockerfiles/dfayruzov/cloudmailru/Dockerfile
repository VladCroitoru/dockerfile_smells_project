FROM ubuntu:trusty

ADD entrypoint.sh /bin/entrypoint.sh

RUN  export DEBIAN_FRONTEND=noninteractive && \
     apt-get update && \
     apt-get -y --force-yes install wget apt-transport-https && \
     wget -qO - https://linuxdesktopcloud.mail.ru/mail.ru-cloud.gpg   | sudo apt-key add - && \
     echo 'deb https://linuxdesktopcloud.mail.ru/deb default free' > /etc/apt/sources.list.d/mail.ru-cloud.list && \
     apt-get update && \
     apt-get -y --force-yes install mail.ru-cloud vnc4server python expect jwm && \
     adduser --disabled-password --gecos "" abc && \
     mkdir -p /home/abc/.vnc && \
     ln -s /usr/bin/jwm /home/abc/.vnc/xstartup && \
     chown -R abc:abc /home/abc 

# Set environment variables
ENV HOME /root
ENV USER root
ENV DISPLAY :0
ENV PGID 1000
ENV PUID 1000

# Define working directory
WORKDIR /root

# Expose VNC port
EXPOSE 5900

# Define default command
ENTRYPOINT ["/bin/entrypoint.sh"]
