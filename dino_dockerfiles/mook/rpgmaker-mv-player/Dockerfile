FROM debian:latest

RUN true \
    && export DEBIAN_FRONTEND=noninteractive \
    && useradd --uid 1000 --create-home docker-user \
    && apt-get update \
    && apt-get install -qy \
        curl \
        libgconf-2-4 \
        libgtk2.0-0 \
        libnotify4 \
        libnss3 \
        pulseaudio-module-x11 \
        xauth \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*dists* \
    && mkdir /rpgmaker-mv \
    && curl http://dl.nwjs.io/v0.12.3/nwjs-v0.12.3-linux-x64.tar.gz | \
        tar xz --strip-components=1 -C /rpgmaker-mv \
    && su -c 'mkdir -p /home/docker-user/.config/pulse/' docker-user \
    && awk ' { print } END { print "enable-shm = no" } ' \
        < /etc/pulse/client.conf \
        > /home/docker-user/.config/pulse/client.conf \
    && true

ADD rpgmaker-mv-player entrypoint.sh /rpgmaker-mv/

ENTRYPOINT ["/bin/sh", "/rpgmaker-mv/entrypoint.sh"]
