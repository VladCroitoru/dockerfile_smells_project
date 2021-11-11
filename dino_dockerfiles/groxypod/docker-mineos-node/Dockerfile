FROM ubuntu:16.04
MAINTAINER GroxyPod <GroxyPod@gmail.com>
# Version v1.0.1

#Install packages
RUN apt-get update && apt-get install -y \
  supervisor \
  rdiff-backup \
  screen \
  openjdk-8-jre-headless \
  rsync \
  git \
  curl \
  rlwrap \
  nano \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#install node from nodesource
RUN curl https://deb.nodesource.com/node_4.x/pool/main/n/nodejs/nodejs_4.7.2-1nodesource1~xenial1_amd64.deb > node.deb \
 && dpkg -i node.deb \
 && rm node.deb

#download mineos from github
RUN mkdir /usr/games/minecraft \
  && cd /usr/games/minecraft \
  && git clone --depth=1 https://github.com/hexparrot/mineos-node.git . \
  && cp mineos.conf /etc/mineos.conf \
  && chmod +x webui.js mineos_console.js service.js

#build npm deps and clean up apt for image minimalization
RUN cd /usr/games/minecraft \
  && apt-get update \
  && apt-get install -y build-essential \
  && npm install \
  && apt-get remove --purge -y build-essential \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#configure and run supervisor
RUN cp /usr/games/minecraft/init/supervisor_conf /etc/supervisor/conf.d/mineos.conf
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]

# Configure user nobody to match unRAID's settings
 RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

#entrypoint allowing for setting of mc password
COPY initialize.sh /initialize.sh
RUN chmod +x /initialize.sh
ENTRYPOINT ["./initialize.sh"]

EXPOSE 8443 25565
VOLUME /var/games/minecraft
