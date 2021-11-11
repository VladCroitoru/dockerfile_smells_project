FROM compulsivecoder/ubuntu-mono:latest

RUN apt-get update && \
  apt-get install -y git wget mono-complete arduino python-configobj python-setuptools git python-jinja2 python-serial python-pip && \
  pip install glob2 && \
  apt-get install picocom

RUN git clone git://github.com/amperka/ino.git && \
  cd ino && \
  make install
