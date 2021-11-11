FROM sofianhw/docker-neon-ipython:latest
MAINTAINER Sofian Hadiwijaya <me@sofianhw.com>

RUN apt-get install libcurl4-openssl-dev clang \
  libopencv-dev libsox-dev \
  -y --no-install-recommends

RUN cd /root && git clone https://github.com/NervanaSystems/aeon.git && cd aeon && \
  python setup.py install

WORKDIR /root/neon
CMD ipython notebook --ip 0.0.0.0 
