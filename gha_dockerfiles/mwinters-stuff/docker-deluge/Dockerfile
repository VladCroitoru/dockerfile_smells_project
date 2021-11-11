FROM linuxserver/deluge 

RUN \
  echo "install packages" && \
  apt-get update && \
  apt-get install -y python3 python3-pip 
RUN \
  pip3 install https://github.com/mwinters-stuff/mnamer/archive/refs/heads/master.zip
RUN \  
  echo "**** cleanup ****" && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/* \
    /provision
