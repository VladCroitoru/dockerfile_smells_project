FROM mono:5

LABEL maintainer Tyler Payne <tyler43636@gmail.com>

# install jackett
RUN apt update && \
  apt install -qy gnupg2 && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \
  echo "deb http://apt.sonarr.tv/ master main" | tee /etc/apt/sources.list.d/sonarr.list && \
  apt -q update && \
  apt install -qy supervisor nzbdrone && \
  apt clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add supervisor file for application
ADD sonarr.conf /etc/supervisor/conf.d/

# add bash scripts
ADD scripts/*.sh /scripts/
RUN chmod +x /scripts/*.sh

# setup home directory so config files are kept in a volume
RUN usermod -m -d /config nobody && \
  mkdir /config

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /data to host defined data path (used to store downloads or use blackhole)
VOLUME /data

# map /media to host defined media path (used to read/write to media library)
VOLUME /media

EXPOSE 8989

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/scripts/init.sh"]
