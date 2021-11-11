FROM buildpack-deps:jessie
MAINTAINER David Martin <davidmartingarcia0@gmail.com>

RUN echo "deb http://pike.esi.uclm.es/arco sid main" > /etc/apt/sources.list.d/pike.list
RUN wget -O- http://pike.esi.uclm.es/arco/key.asc | apt-key --keyring /etc/apt/trusted.gpg.d/pike.gpg add -
RUN apt-get update && apt-get install esi-tfg -y --no-install-recommends && apt-get clean autoclean -y && rm -rf /var/lib/{apt,dpkg,cache,log}
