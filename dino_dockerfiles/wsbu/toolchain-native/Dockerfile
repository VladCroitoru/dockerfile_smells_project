FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --yes --no-install-recommends \
    apt-transport-https \
    autoconf \
    automake \
    autopoint \
    bc \
    bison \
    ca-certificates \
    ccache \
    clang-tidy \
    curl \
    docbook-xml \
    docbook-xsl \
    doxygen \
    fakeroot \
    flex \
    g++ \
    gawk \
    gcc \
    gcovr \
    gettext \
    git-core \
    golang-1.10 \
    gperf \
    graphviz \
    groff \
    inotify-tools \
    intltool \
    kmod \
    liblist-moreutils-perl \
    liblzo2-dev \
    libtool \
    libxml-dom-perl \
    libxml2-utils \
    lua5.3 \
    make \
    mtd-utils \
    net-tools \
    nodejs \
    npm \
    openssh-client \
    pkg-config \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    rsync \
    scons \
    sudo \
    texinfo \
    time \
    u-boot-tools \
    uuid-dev \
    w3m \
    wget \
    xsltproc \
    xutils-dev \
    xz-utils \
    zip \
    zlib1g-dev \
  && rm --recursive --force /var/lib/apt/lists/* \
  && npm install -g showdown \
  && pip3 --no-cache-dir install conan==1.21.0 \
  && ln -sf /bin/bash /bin/sh \
  && ln -sf /usr/bin/lua5.3 /usr/bin/lua \
  && ln -sf /usr/lib/go-1.10/bin/gofmt /usr/bin/gofmt \
  && ln -sf /usr/lib/go-1.10/bin/go /usr/bin/go \
  && wget https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 -O /usr/local/bin/dep \
  && chmod +x /usr/local/bin/dep


RUN mkdir /src \
  && wget --quiet -O /src/cmake.sh https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4-Linux-x86_64.sh \
    && sh /src/cmake.sh --prefix=/usr/local --exclude-subdir --skip-license \
  && git clone https://github.com/wsbu/cross-browser.git \
      --branch x419_z1 --depth 1 /src/crossbrowser \
    && cd /src/crossbrowser/x/xc \
    && gcc -c xc.c -O2 \
    && gcc -o xc xc.o -O2 \
    && cp --force xc /bin \
    && strip /bin/xc \
    && mkdir --parents /lib/crossbrowser \
    && cp --archive /src/crossbrowser/x/lib/*.js /lib/crossbrowser \
    && cp --archive /src/crossbrowser/x/lib/old/*.js /lib/crossbrowser

ENV HOME=/home/captain \
  CONAN_PRINT_RUN_COMMANDS=1
COPY conan/profile "${HOME}/.conan/profiles/default"
COPY conan/settings.yml "${HOME}/.conan/settings.yml"

RUN groupadd --gid 1000 captain \
  && useradd --home-dir "${HOME}" --uid 1000 --gid 1000 captain \
  && mkdir --parents "${HOME}/.ssh" \
  && cp /root/.bashrc /root/.profile "${HOME}" \
  && conan config set general.revisions_enabled=True \
  && chown --recursive captain:captain "${HOME}" \
  && chmod --recursive 777 "${HOME}" \
  && echo "ALL ALL=NOPASSWD: ALL" >> /etc/sudoers


COPY start.sh /start.sh
ENTRYPOINT ["/start.sh"]

LABEL "net.redlion.family"="controller"
LABEL "net.redlion.controller.platform"="x86_64"
LABEL "net.redlion.controller.image"="toolchain"
