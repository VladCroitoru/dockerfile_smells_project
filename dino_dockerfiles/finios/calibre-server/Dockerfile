FROM ubuntu:20.04

# example 4.15.0: calibre_version="version=4.15.0"
# example latest: calibre_version=""
ARG calibre_version
ENV calibre_version=$calibre_version \
    TZ=Europe/Berlin

LABEL maintainer="finios" \
      description="calibre-server"

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && \
    apt-get -y install \
		wget \
		python3 \
		xz-utils \
		imagemagick \
		xdg-utils && \
    apt-get -y install --no-install-recommends \
		dbus \
		libnss3 \
		sqlite3 \
		libxcb-icccm4 \
		libxcb-image0 \
		libxcb-keysyms1 \
		libxcb-randr0 \
		libxcb-render-util0 \
		libxcb-xinerama0 \
		python3-xdg \
		bash-completion && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/src/* && \
    mkdir -p /usr/share/desktop-directories

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin ${calibre_version} && \
    rm /tmp/calibre* -Rf 2>&1 >/dev/null

WORKDIR /opt/calibre

COPY * /

RUN mkdir -p /calibre-lib && \
    mkdir -p /calibre-config && \
    chgrp -R 100 /calibre-lib && \
    chgrp -R 100 /calibre-config && \
    chmod -R 755 /calibre-lib && \
    chmod -R 755 /calibre-config && \
    chmod 755 /docker-entrypoint.sh

VOLUME ["/calibre-lib", "/calibre-config"]

EXPOSE 8080

ENV PORT=8080 \
    PREFIX="/" \
    LIBRARY="/calibre-lib" \
    USERDB="server-users.sqlite" \
    AUTH="disable-auth" \
    AUTH_USER="root" \
    AUTH_PASSWORD="root" \
    BANAFTER=5 \
    BANFOR=30 \
    AJAXTIMEOUT=60 \
    TIMEOUT=120 \
    NUMPERPAGE=50 \
    MAXOPDS=30 \
    OTHERPARAM= \
    CALIBRE_OVERRIDE_LANG="en" \
    CALIBRE_CONFIG_DIRECTORY="/calibre-config/calibre"

ENTRYPOINT /docker-entrypoint.sh
CMD [""]
