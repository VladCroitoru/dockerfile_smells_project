FROM ubuntu:focal
LABEL MAINTAINER='William Dizon <wdchromium@gmail.com>'

#update and accept all prompts
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
  supervisor \
  rdiff-backup \
  screen \
  rsync \
  git \
  curl \
  rlwrap \
  openjdk-16-jre-headless \
  openjdk-8-jre-headless \
  ca-certificates-java \
  python3-minimal \
  sudo \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#install node from nodesource following instructions: https://github.com/nodesource/distributions#debinstall
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#download mineos from github
ADD https://api.github.com/repos/cpburnz/mineos-node/git/refs/heads/master mineos-node.json
RUN mkdir /usr/games/minecraft \
  && cd /usr/games/minecraft \
  && git clone --depth=1 https://github.com/cpburnz/mineos-node.git . \
  && cp mineos.conf /etc/mineos.conf \
  && chmod +x webui.js mineos_console.js service.js run_webui.py shutdown_servers.sh

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

#entrypoint allowing for setting of mc password
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8443 25565-25570
VOLUME /var/games/minecraft

ENV USER_PASSWORD=random_see_log USER_NAME=mc USER_UID=1000 USE_HTTPS=true SERVER_PORT=8443
