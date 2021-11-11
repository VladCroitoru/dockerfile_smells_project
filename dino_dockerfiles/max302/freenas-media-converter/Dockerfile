FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /

RUN apt-get -qq update \
  && apt-get install -y \
    libav-tools \
    curl \
  && apt-get clean autoclean \
  && apt-get autoremove -y --purge \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/

ADD entrypoint.sh .
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

LABEL org.freenas.interactive="false"                             \
      org.freenas.version="latest"                                \
      org.freenas.upgradeable="false"                             \
      org.freenas.expose-ports-at-host="false"                    \
      org.freenas.autostart="false"                               \
      org.freenas.volumes="[						                          \
          {								                                        \
              \"name\":\"/media\",				                        \
              \"descr\": \"Storj configuration files\"			      \
          }                                                       \
      ]"                                                          \
      org.freenas.settings="[ 						                        \
          {								                                        \
              \"env\": \"MEDIA_CONV\",		                        \
              \"descr\": \"Media folder\",	               	      \
              \"optional\": true					                        \
          }								                                        \
      ]"
