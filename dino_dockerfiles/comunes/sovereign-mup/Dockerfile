#FROM meteorhacks/meteord:base #Does not support meteor 1.4
FROM abernix/meteord:base
RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install wget -y
RUN curl https://21.co | sh
