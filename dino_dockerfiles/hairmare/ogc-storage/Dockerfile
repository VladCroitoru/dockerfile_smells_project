FROM hairmare/gentoo
MAINTAINER Lucas Bickel <hairmare@purplehaze.ch>

# configure rsync

COPY rsyncd.conf /etc/rsyncd.conf

RUN useradd --create-home --system --base-dir=/var/lib ogc; \
    su -l ogc -c 'mkdir /var/lib/ogc/{dist,run}'

# setup container

VOLUME /var/lib/ogc/dist

ENTRYPOINT [ "/usr/bin/rsync" ]

EXPOSE 873
