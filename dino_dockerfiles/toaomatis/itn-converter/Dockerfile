FROM suchja/wine:latest
MAINTAINER Mathijs de Kruyf <hpmdekruyf+docker@gmail.com>

ENV ITN_CONVERTER_VERSION 1.94
ENV ITN_DOWNLOAD_FILE itnconv194.zip

USER root

# Install cabextract while winetricks needs it
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    cabextract && \
  rm -rf /var/lib/apt/lists/*

USER xclient

# Download and extract ITN Converter
RUN \
  curl -o itnconv.zip http://download.benitools.info/$ITN_DOWNLOAD_FILE && \
  unzip itnconv.zip && \
  rm itnconv.zip

# Add startup script
ADD scripts/init.sh /home/xclient/scripts/init.sh

ENTRYPOINT ["/home/xclient/scripts/init.sh"]
