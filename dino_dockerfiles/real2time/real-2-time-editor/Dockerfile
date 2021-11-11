FROM ubuntu:trusty

MAINTAINER real2time <info@real2time.com>

# This container
ENV R2T_EDITOR_LISTEN_ADDRESS 0.0.0.0
ENV R2T_EDITOR_LISTEN_PORT 8080

# Linked containers
ENV R2T_STORM_LISTEN_HOST r2t_storm
ENV R2T_EDITOR_DATABASE_HOST mongo

# Remote services
ENV STORM_SERVER_UI_PORT 8080
ENV STORM_SERVER_UI_HOST 127.0.0.1
ENV STORM_PROXY_SERVER_UI_PORT 8081

RUN apt-get update; apt-get install -y git openjdk-7-jdk wget vim nodejs nodejs-legacy npm openssh-server supervisor

RUN mkdir -p /var/run/sshd /var/log/supervisor

RUN echo 'root:real2time' | chpasswd; sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN cd /opt; git clone https://github.com/real2time/real-2-time-editor.git; cd real-2-time-editor; npm install .

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE $R2T_EDITOR_LISTEN_PORT
EXPOSE $STORM_PROXY_SERVER_UI_PORT
EXPOSE 22