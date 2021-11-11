FROM alpine:3.9
MAINTAINER fukusaka

LABEL \
  org.label-schema.name="python-moinmoin" \
  org.label-schema.vendor="fukusaka" \
  org.label-schema.vcs-url="https://github.com/fukusaka/python-moinmoin" \
  org.label-schema.version="2.0"

ARG MOIN_UID=1000
ARG MOIN_GID=1000

ENV MOIN_VERSION=1.9.10

RUN set -x \
  && apk add --update --nocache openrc \
  && sed -i 's/^\(tty\d\d*\:\:\)/#\1/g' /etc/inittab \
  && sed -i \
    # Change subsystem type to "docker"
    -e 's/#rc_sys=""/rc_sys="docker"/g' \
    # Allow all variables through
    -e 's/#rc_env_allow=".*"/rc_env_allow="\*"/g' \
    # loopback and net are already there, since docker handles the networking
    -e 's/#rc_provide=".*/rc_provide="loopback net"/g' \
    /etc/rc.conf \
  && rm -f /etc/init.d/hwdrivers \
        /etc/init.d/hwclock \
        /etc/init.d/hwdrivers \
        /etc/init.d/modules \
        /etc/init.d/modules-load \
        /etc/init.d/modloop \
  && sed -i 's/\(hostname $opts\)/#\1/' /etc/init.d/hostname \
  && sed -i 's/^\([ \t]*\)cgroup_add_service/\1#cgroup_add_service/g' /lib/rc/sh/openrc-run.sh \
  && sed -i 's/VSERVER/DOCKER/Ig' /lib/rc/sh/init.sh

RUN set -x \
  && apk add --update --nocache uwsgi-python py-pip \
  && pip install moin==$MOIN_VERSION \
  && addgroup -g ${MOIN_UID} moin \
  && adduser -S -G moin -u ${MOIN_GID} moin \
  && install -o moin -g moin -d /srv/moin/mywiki \
  && install -o moin -g moin -d /srv/moin/mywiki/html \
  && cp -r /usr/share/moin/data /srv/moin/mywiki \
  && cp -r /usr/share/moin/underlay /srv/moin/mywiki \
  && chown -R moin:moin /srv/moin/mywiki \
  && chmod -R ug+rwX,o-rwx /srv/moin/mywiki \
  && install -o moin -g moin -d /var/run/moin \
  && install -o root -g moin -m 775 -d /var/log/moin \
  && ln -s /etc/init.d/uwsgi /etc/init.d/moin \
  && rc-update add moin default \
  && echo -e 'user=moin\ngroup=moin\nlogfile=/var/log/moin/moin.log' >> /etc/conf.d/moin \
  && sed -i -e "/^#sys\.path\.insert(0, '\/path\/to\/farmconfigdir')/asys.path.insert(0, '/etc/moin')" \
      /usr/share/moin/server/moin*

COPY conf/uwsgi-moin.ini /etc/moin/uwsgi.ini
COPY conf/moin-farmconfig.py /etc/moin/farmconfig.py
COPY conf/moin-mywiki.py /etc/moin/mywiki.py

RUN set -x \
  && apk add --update --nocache nginx \
  && mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf-orig \
  && addgroup nginx moin

COPY conf/nginx-moin.conf /etc/nginx/conf.d/moin.conf

ENV MOIN_UID=${MOIN_UID}
ENV MOIN_GID=${MOIN_GID}
ENV USE_NGINX=yes
ENV SETUP_WIKI=yes
ENV WIKI_ADMIN=admin
ENV WIKI_ADMIN_PASS=moinmoin
ENV WIKI_ADMIN_EMAIL=amdin@example.org
ENV WIKI_ACL_RIGHTS_BEFORE="admin:read,write,delete,revert,admin"
ENV WIKI_ACL_RIGHTS_DEFAULT="Known:read,write,delete,revert All:read"

COPY conf/init.sh /init.sh
RUN chmod +x /init.sh

VOLUME "/srv/moin/mywiki/data/pages"

EXPOSE 80 3031

CMD ["/init.sh"]
