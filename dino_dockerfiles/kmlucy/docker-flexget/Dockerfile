FROM smdion/docker-flexget

RUN apt-get -qq update \
  && apt-get install -y deluge-common \
  && apt-get clean \ 
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/
