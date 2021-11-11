# This will build the witness_node in a docker image. Make sure you've already
# checked out the submodules before building.

#FROM l3iggs/archlinux:latest
#MAINTAINER Nathan Hourt <nathan@followmyvote.com>#

#RUN pacman -Syu --noconfirm gcc make autoconf automake cmake ninja boost libtool git#

#ADD . /bitshares-2
#WORKDIR /bitshares-2
#RUN cmake -G Ninja -DCMAKE_BUILD_TYPE=Release .
#RUN ninja witness_node || ninja -j 1 witness_node#

#RUN mkdir /data_dir
#ADD docker/default_config.ini /default_config.ini
#ADD docker/launch /launch
#RUN chmod a+x /launch
#VOLUME /data_dir#

#EXPOSE 8090 9090#

#ENTRYPOINT ["/launch"]

FROM educatedwarrior/invictus_image:1.59
MAINTAINER educatedwarrior 

# Configuration variables
#test or prod for NODE_TYPE
ENV NODE_TYPE=prod
ENV LANG=en_US.UTF-8
ENV WORKDIR /opt/bitshares/bin
ENV DATADIR /opt/bitshares/bin/witness_node_data_dir
ENV LOGDIR /opt/bitshares/bin/witness_node_data_dir/logs

ENV TEST_SEED 51.15.61.160:1776
ENV PROD_SEED seeds.bitshares.eu:1776

LABEL org.freenas.interactive="false"       \
      org.freenas.version="1.59.1.0000"      \
      org.freenas.upgradeable="true"        \
      org.freenas.expose-ports-at-host="true"   \
      org.freenas.autostart="true"      \
      org.freenas.web-ui-protocol="http"    \
      org.freenas.web-ui-port=8090     \
      org.freenas.web-ui-path=""     \
      org.freenas.port-mappings="8090:8090/tcp"         \
      org.freenas.volumes="[                    \
          {                         \
              \"name\": \"${DATADIR}\",              \
              \"descr\": \"Data directory\"           \
          }                         \
      ]"                            \
      org.freenas.settings="[                   \
          {                         \
              \"env\": \"NODE_TYPE\",                  \
              \"descr\": \"test or prod.  Default value test\",       \
              \"optional\": false                \
          },                            \
          {                         \
              \"env\": \"TEST_SEED\",                \
              \"descr\": \"Default value 51.15.61.160:1776\",          \
              \"optional\": true                \
          },                            \
          {                         \
              \"env\": \"PROD_SEED\",                \
              \"descr\": \"Default value seeds.bitshares.eu:1776\",         \
              \"optional\": true                \
          }                            \
      ]"

#Build blockchain source
RUN \
	cd /tmp && git clone https://github.com/bitshares/bitshares-core.git && \
	cd bitshares-core && \
	git submodule update --init --recursive && \
	cmake -DBOOST_ROOT="$BOOST_ROOT" -DCMAKE_BUILD_TYPE=Release . && \
	make witness_node cli_wallet

# Make binary builds available for general-system wide use 
RUN \
	cp /tmp/bitshares-core/programs/witness_node/witness_node /usr/bin/witness_node && \
	cp /tmp/bitshares-core/programs/cli_wallet/cli_wallet /usr/bin/cli_wallet

RUN mkdir -p "$DATADIR"
#COPY /docker/default_config.ini genesis-test.json genesis.json /
COPY /docker/default_config.ini /config.ini
COPY genesis.json /
COPY /docker/entrypoint.sh /sbin
RUN cd "$WORKDIR" && chmod +x /sbin/entrypoint.sh
VOLUME "$DATADIR"
EXPOSE 8090
CMD ["/sbin/entrypoint.sh"]
