FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install skewer
RUN \
  wget -c https://downloads.sourceforge.net/project/skewer/Binaries/skewer-0.2.2-linux-x86_64 && \
  chmod +x skewer-0.2.2-linux-x86_64 && \
  cp skewer-0.2.2-linux-x86_64 /usr/local/bin/skewer
