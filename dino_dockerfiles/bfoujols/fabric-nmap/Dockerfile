FROM ubuntu:14.04.3
MAINTAINER Benoit Foujols "benoit@foujols.com"

# Up to date
RUN (apt-get update \
  && apt-get upgrade -y -q \
  && apt-get dist-upgrade -y -q \
  && apt-get -y -q autoclean \
  && apt-get -y -q autoremove)

# Install to stack
RUN apt-get install -y -q ssh \
  git \
  python-pip \
  python-dev \
  build-essential \
  nmap \
  wget \
  zip

# Install to pre requis
RUN pip install fabric \
  python-nmap \
  ecdsa \
  ssh \
  pycrypto

# Install to nfab
RUN wget -Lok https://github.com/bfoujols/fabric-nmap/archive/master.zip
RUN unzip master.zip -d /opt
RUN rm -f master.zip
RUN echo "alias nfab='python /opt/fabric-nmap-master/nfab.py'" >> /root/.bashrc

ENTRYPOINT ["/bin/bash"]