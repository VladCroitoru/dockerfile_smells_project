FROM steigr/docker-volume-plugin-shell

# tools for mounting in different mount namespace
RUN  apk add --update util-linux jq && cp /usr/bin/nsenter /tmp && apk del util-linux && mv /tmp/nsenter /usr/bin/nsenter && rm -rf /var/cache/apk/*

# Torus Tools
ADD  torusctl          /tool/torusctl
ADD  torusblk          /tool/torusblk
ADD  docker            /tool/docker
ADD  pause             /tool/pause
ADD  start-stop-daemon /sbin/start-stop-daemon

ENV  PATH=$PATH:/tool:/helpers:/handler

# configure shell stack
ENV  DRIVER_NAME torus
ENV  MOUNTS /var/lib/torus-volume-plugin

# add the event handlers
ADD  helpers/ /helpers
ADD  driver/  /driver
ADD  handler/ /handler
