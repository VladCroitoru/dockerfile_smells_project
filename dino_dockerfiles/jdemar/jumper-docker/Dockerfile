FROM ubuntu:17.10

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:team-gcc-arm-embedded/ppa

RUN apt-get update && apt-get install -y gcc-arm-embedded python-setuptools python-dev

RUN easy_install pip
RUN pip install jumper

RUN apt-get clean && \
  rm -rf /var/lib/apt
