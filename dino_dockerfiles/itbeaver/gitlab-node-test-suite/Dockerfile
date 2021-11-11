FROM node:8-stretch

MAINTAINER Alexander Bobrov, ITBeaver <al.bobrov@itbeaver.co>

ENV NPM_CONFIG_LOGLEVEL info
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
  apt-get install -y libgtk-3-dev libgconf-2-4 \
    libasound2 libxtst6 libxss1 libnss3 xvfb build-essential

ENV DISPLAY :99

COPY entrypoint.sh /
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
