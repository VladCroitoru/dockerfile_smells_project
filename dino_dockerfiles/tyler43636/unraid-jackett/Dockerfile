FROM mono:5.20

MAINTAINER Tyler Payne <tyler43636@gmail.com>

# install jackett
RUN apt-get -q update && \
  apt-get install -qy wget libcurl4-openssl-dev bzip2 supervisor && \
  export JACKETTDL=$(wget -q https://api.github.com/repos/Jackett/Jackett/releases/latest -O - | grep browser_download_url | head -n 1 | cut -d '"' -f 4) && \
  wget --no-verbose -P /tmp $JACKETTDL && \
  tar -xvf /tmp/Jackett* -C /opt && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add supervisor file for application
ADD jackett.conf /etc/supervisor/conf.d/

# add bash scripts
ADD scripts/*.sh /scripts/
RUN chmod +x /scripts/*.sh

# setup home directory so config files are kept in a volume
RUN usermod -m -d /config nobody && \
  mkdir /config

VOLUME /config

EXPOSE 9117

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/scripts/init.sh"]

HEALTHCHECK CMD curl --fail http://localhost:9117/UI/Dashboard || exit 1
