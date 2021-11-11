FROM ubuntu:16.04
MAINTAINER felicitychou<felicitychou@hotmail.com>

RUN apt-get update && apt-get install -y \
tcpdump \
python \
software-properties-common \
&& dpkg --add-architecture i386 \
&& add-apt-repository ppa:wine/wine-builds \
&& apt-get update \
&& apt-get install -y --install-recommends winehq-devel \
&& apt-get purge -y software-properties-common \
&& apt-get clean -y \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/*

RUN wine wineboot --init
