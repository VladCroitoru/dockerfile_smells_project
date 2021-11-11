FROM node:6-alpine

RUN \
  apk add --no-cache --update git python openssl-dev g++ make bash supervisor && \
  npm config set progress false && \
  npm install --global --unsafe dat storjshare-daemon && \
  npm cache clean && \
  apk del openssl-dev git g++ make bash python && \
  rm -rf /var/cache/apk/* /tmp/* /root/.node-gyp

COPY supervisord.conf /etc/supervisord.conf
COPY storj-start /usr/sbin/storj-start

VOLUME /mnt/share
VOLUME /etc/storj

EXPOSE 4000/tcp

LABEL org.freenas.interactive="false" \
      org.freenas.version="1.3" \
      org.freenas.upgradeable="true" \
      org.freenas.expose-ports-at-host="false" \
      org.freenas.autostart="true" \
      org.freenas.port-mappings="4000:4000/tcp,4001:4001/tcp,4002:4002/tcp,4003:4003/tcp" \
      org.freenas.volumes="[						\
          {								\
              \"name\": \"/etc/storj\",				\
              \"descr\": \"Config storage location\"			\
          },								\
          {								\
              \"name\": \"/mnt/share\",				\
              \"descr\": \"Data storage location\"			\
          }								\
      ]"

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
