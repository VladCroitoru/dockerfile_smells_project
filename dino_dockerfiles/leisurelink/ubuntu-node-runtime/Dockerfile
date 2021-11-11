FROM leisurelink/baseimage-node:latest
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

# Indicate where your node app will located in the container. The default is:
#   /opt/app
#
# You may also specify the entrypoint file name. The default is:
#   app.js
#
# With the defaults in place, the container will start your node application
# as a service somewhat similar to the following command line:
#   node /opt/app/app.js

ENV NODE_SERVICE_ROOT=/opt/app \
    NODE_SERVICE_ENTRYPOINT=app.js

COPY rootfs /

RUN set -ex && \
  groupadd --system node && \
  useradd --system -g node node && \
  chmod a+x /etc/service/nodejs/run && \
  rm -rf /var/lib/apt/lists/* \
         /var/tmp/* \
         /tmp/*

# start service manager, our run script will change user to node
CMD ["/sbin/my_init"]
