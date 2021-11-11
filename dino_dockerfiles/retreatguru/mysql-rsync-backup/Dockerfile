FROM alpine
RUN apk add --no-cache rsync openssh
ENV RSYNC_OPTIONS="-a --info=progress2 --exclude='*.pem' --delete"
COPY bin/* /usr/bin/
ENTRYPOINT tail -f /dev/null
