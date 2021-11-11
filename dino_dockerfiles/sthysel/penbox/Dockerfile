FROM ubuntu:latest
MAINTAINER sthysel <sthysel@gmail.com>
ENV REFRESHED_AT 2016-09-10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
  sudo \
  apt-transport-https \
  build-essential \
  cmake \
  git \
  tree \
  vim \
  wireshark \
  ssh \
  nmap
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# home env
RUN useradd -ms /bin/bash pen && echo "pen:pen" | chpasswd && adduser pen sudo

ENV HOME /home/pen
RUN mkdir -p ${HOME} ${HOME}/bin ${HOME}/include
WORKDIR ${HOME}
COPY pentest.sh ${HOME}/
USER pen

ENTRYPOINT ["./pentest.sh"]
CMD ["nmap"]
