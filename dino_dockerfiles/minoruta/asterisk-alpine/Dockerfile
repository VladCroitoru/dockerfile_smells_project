ARG VERSION_OPENRC=latest
FROM dockage/alpine-openrc:$VERSION_OPENRC
MAINTAINER KINOSHITA minoru <5021543+minoruta@users.noreply.github.com>
ARG VERSION_ASTERISK=15.1.5-r1

WORKDIR /root
COPY volume/etc/asterisk /etc/asterisk

RUN apk add --no-cache asterisk=$VERSION_ASTERISK \
&& rc-status \
&& rc-update add asterisk default \
&& touch /run/openrc/softlevel

CMD asterisk -c
