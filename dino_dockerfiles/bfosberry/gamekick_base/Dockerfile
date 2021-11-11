# Gamekick base repo
#
# VERSION 0.1

FROM ubuntu
MAINTAINER bfosberry

USER root

RUN groupadd -r appuser && useradd -r -m -g appuser appuser
RUN echo "appuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers

RUN apt-get update && apt-get -y install \ 
  wget \
  curl \
  build-essential \ 
  libxml2-dev \
  libxslt-dev \
  screen

# install confd
RUN wget https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-amd64
RUN mv confd-0.7.1-linux-amd64 /usr/local/bin/confd && chmod +x /usr/local/bin/confd

ENV PATH /opt/scripts/:$PATH

ENV DATA_FOLDER /opt/data/
RUN mkdir -p $DATA_FOLDER

RUN chown -R appuser:appuser /opt/data/
RUN chmod g+w /opt
RUN chown appuser:appuser -R /opt

USER appuser
ENV USERNAME appuser
ENV HOME /home/$USERNAME

ADD ./scripts /opt/scripts

ENTRYPOINT ["/opt/scripts/start.sh"]
