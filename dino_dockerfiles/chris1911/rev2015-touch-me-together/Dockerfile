FROM node:wheezy

MAINTAINER chris1911@users.noreply.github.com

RUN echo >> /etc/apt/apt.conf.d/00aptitude "APT::Install-Recommends \"0\";" && \
    echo >> /etc/apt/apt.conf.d/00aptitude "APT::Install-Suggests \"0\";"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils git

RUN \
   mkdir /rev2015 && \
   cd /rev2015 && \
   git clone https://github.com/tmp-demo/touch-me-together.git && \
   cd touch-me-together && \
   npm install

EXPOSE 3000

CMD cd /rev2015/touch-me-together && node .
