FROM debian:latest
RUN apt-get -yq update && apt-get -yq upgrade

RUN apt-get -yq install git
RUN apt-get -yq install build-essential
RUN apt-get -yq install libncurses5-dev
RUN apt-get -yq install lua5.1-dev
RUN apt-get -yq install libncursesw5-dev
RUN cd /usr/local/src \
  && git clone https://github.com/CleverRaven/Cataclysm-DDA.git
WORKDIR /usr/local/src/Cataclysm-DDA
RUN  make #LUA=1
CMD ./cataclysm-launcher
