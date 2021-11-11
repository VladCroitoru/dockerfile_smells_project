FROM ubuntu:latest AS stg1



# set environment variables

ENV \
  DEBIAN_FRONTEND='noninteractive' \
  HOME=/home/ \
  LANG='en_US.UTF-8' \
  LANGUAGE='en_US.UTF-8' \
  TERM='xterm' \
  TZ='Asia/Kolkata'
###



#WORKDIR /home/



# set argument for s6

ARG S6_VERSION='v2.2.0.3'
ARG S6_ARCH='amd64'
###
ADD https://tgbg.netlify.app/root/home/Base_Setup_.Sh ~/



# adding s6

ADD https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-${S6_ARCH}-installer /tmp/

RUN \
  chmod +x /tmp/s6-overlay-amd64-installer && \
    /tmp/s6-overlay-amd64-installer / > /dev/null && \
  rm -rf /tmp/*
###



COPY *_.sh /home/



RUN find ~/ -type f -iname "*_.sh" -exec chmod +x {} \;
RUN ~/setup_.sh



COPY root/ /
COPY site-apps/ /etc/nginx/site-apps/


FROM scratch

COPY --from=stg1 / /

CMD echo $PORT && ulimit -v 402653184 && /init

###




