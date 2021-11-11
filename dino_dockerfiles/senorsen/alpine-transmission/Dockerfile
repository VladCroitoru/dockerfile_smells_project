FROM alpine:latest

LABEL maintainer="Senorsen <senorsen.zhang@gmail.com>"

RUN apk add --no-cache transmission-daemon \
  && echo '#torrent_upload_file, label[for="torrent_upload_file"] {display: block !important;}' >> /usr/share/transmission/web/style/transmission/mobile.css
# dirty hack for mobile ui

RUN mkdir -p /transmission/downloads \
  && mkdir -p /transmission/incomplete \
  && mkdir -p /etc/transmission-daemon

COPY src/ .

VOLUME ["/transmission/downloads"]
VOLUME ["/transmission/incomplete"]
VOLUME ["/etc/transmission-daemon"]

EXPOSE 9091 51413/tcp 51413/udp

ENV USERNAME admin
ENV PASSWORD password

RUN chmod +x /start.sh
CMD ["/start.sh"]
