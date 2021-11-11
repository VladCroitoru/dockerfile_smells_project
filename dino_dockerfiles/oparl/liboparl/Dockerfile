FROM debian:testing-slim

# Set system locale to something sensible (en_US.UTF-8)

ARG locale='en_US.UTF-8'
ENV DEBIAN_FRONTEND noninteractive

ADD . /liboparl
WORKDIR /liboparl
RUN apt update && apt install -y --no-install-recommends \
    locales && \
    echo "${locale} UTF-8" > /etc/locale.gen && \
    locale-gen ${locale} && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=${locale} && \
    export LC_ALL=${locale} && \
    apt install -y --no-install-recommends \
    valac \
    valadoc \
    gobject-introspection \
    libjson-glib-dev \
    libgirepository1.0-dev \
    meson \
    gettext \
    git && \
    mkdir build && \
    cd build && \
    meson --buildtype=release --prefix=/usr && \
    ninja && \
    ninja install && \
    rm -rf /usr/share/meson && \
    apt remove --purge -y \
    build-essential \
    ninja \
    valac \
    valadoc \
    libjson-glib-dev \
    libgirepository1.0-dev \
    meson \
    gettext \
    git && \
    apt autoremove -y && \
    apt install -y --no-install-recommends \
    json-glib-1.0 \
    gir1.2-json-1.0 && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /liboparl && \
    apt clean
