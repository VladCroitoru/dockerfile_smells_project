# This will build the witness_node in a docker image. Make sure you've already
# checked out the submodules before building.

FROM educatedwarrior/invictus_image:1.59
MAINTAINER educatedwarrior 

# Configuration variables
#witness or seed for NODE_TYPE`
#test or prod for ENVIRONMENT
ENV NODE_TYPE witness
ENV ENVIRONMENT test
ENV LANG en_US.UTF-8
ENV WORKDIR /opt/peerplays/bin
ENV DATADIR /opt/peerplays/bin/witness_node_data_dir
ENV LOGDIR /opt/peerplays/bin/witness_node_data_dir/logs

ENV TEST_SEED seed.ppytest.blckchnd.com:7778 
ENV PROD_SEED 213.184.225.234:59500

LABEL org.freenas.interactive="false"       \
      org.freenas.version="1.59.1.0002"      \
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
              \"descr\": \"witness or seed.  Default value witness\",       \
              \"optional\": false                \
          },                            \
          {                         \
              \"env\": \"TEST_SEED\",                \
              \"descr\": \"Default value seed.ppytest.blckchnd.com:7778\",          \
              \"optional\": true                \
          },                            \
          {                         \
              \"env\": \"PROD_SEED\",                \
              \"descr\": \"Default value 213.184.225.234:59500\",         \
              \"optional\": true                \
          }                            \
      ]"

#Build blockchain source for PROD
RUN \
	cd /tmp && \
  git clone https://github.com/pbsa/peerplays.git && \
	cd peerplays && \
	git submodule update --init --recursive && \
	cmake -j 8 -DBOOST_ROOT="$BOOST_ROOT" -DCMAKE_BUILD_TYPE=Release . && \
	make witness_node cli_wallet

#Build blockchain source for TEST 
RUN \
  mkdir /tmp/testbuild && \
  cd /tmp/testbuild && \
  git clone -b testnet-draft https://github.com/ppytest/peerplays.git && \
	cd peerplays && \
	git submodule update --init --recursive && \
	cmake -j 8 -DBOOST_ROOT="$BOOST_ROOT" -DCMAKE_BUILD_TYPE=Release . && \
	make witness_node cli_wallet


# Make binary builds available for general-system wide use , and clean up
#RUN \
#	cp /tmp/peerplays/programs/witness_node/witness_node /usr/bin/witness_node && \
#	cp /tmp/peerplays/programs/cli_wallet/cli_wallet /usr/bin/cli_wallet 
	
# Cleanup	
#RUN \	
	#apt-get autoremove -y \
	#&& apt-get clean \
	#&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
  
RUN mkdir -p "$DATADIR"
RUN touch genesis-test.json
RUN touch genesis.json
COPY genesis.json /
COPY /docker/prod_config.ini /
COPY /docker/test_config.ini /
COPY /docker/entrypoint.sh /sbin
RUN cd "$WORKDIR" && chmod +x /sbin/entrypoint.sh
VOLUME "$DATADIR"
EXPOSE 8090
CMD ["/sbin/entrypoint.sh"]
