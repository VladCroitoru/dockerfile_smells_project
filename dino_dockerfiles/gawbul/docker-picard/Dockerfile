FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install picard
RUN \
  wget -c https://github.com/broadinstitute/picard/releases/download/2.9.0/picard.jar && \
  echo '#!/bin/bash\njava -jar /usr/local/bin/picard.jar' > picard && \
  chmod +x picard picard.jar && \
  cp picard picard.jar /usr/local/bin
