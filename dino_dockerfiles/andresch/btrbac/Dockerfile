# =================================
# Dockerfile for btrbac
# =================================

FROM docker.io/debian:stretch-slim 

MAINTAINER Andreas Schmidt <andresch@users.noreply.github.com>

LABEL description="A dockerized tool to backup btrfs subvolumes" version="0.1"

RUN apt-get update && apt-get install -y \
  btrfs-tools \
  curl \
  libboost-filesystem1.62.0 \ 
  libboost-program-options1.62.0 \ 
  libboost-regex1.62.0 \ 
  libboost-system1.62.0 \ 
  libcurl3 \ 
  libssl1.0 \
  zip \
  && rm -rf /var/lib/apt/lists/*

# Ensure that we get a cache invalidation when there's new content available
ADD https://api.github.com/repos/ncw/rclone/branches/stable /dev/null

RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip && \
  unzip rclone-current-linux-amd64.zip && \
  cd rclone-*-linux-amd64 && \
  mv rclone /usr/local/bin && \
  cd .. && \
  rm -rf rclone-*-linux-amd64 && \
  rm rclone-current-linux-amd64.zip && \
  chmod 755 /usr/local/bin/rclone

RUN touch /rclone.conf
  
# Which subvolume are we going to backup
VOLUME /subvolume

# Where are we going to store the backups
VOLUME /backup

# Where do we find the rclone configuration
# VOLUME /rclone.conf

ENTRYPOINT [ "/usr/local/bin/btrbac" , "-s" , "/subvolume" , "-b", "/backup" , "-c", "/rclone.conf" ]

CMD [ -h ]

COPY btrbac /usr/local/bin


