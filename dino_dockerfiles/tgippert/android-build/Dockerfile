FROM openjdk:8-jdk

# Install Android Platform tools
RUN mkdir -p /tmp \
    && curl -SsL --retry 5 https://dl.google.com/android/repository/platform-tools-latest-linux.zip > /tmp/platform-tools-latest-linux.zip \
    && unzip /tmp/platform-tools-latest-linux.zip -d /usr/local/bin \
    && rm -rf /tmp/platform-tools-latest-linux.zip

ENV PATH=/usr/local/bin/platform-tools:$PATH

# Install OS packages according to https://wiki.lineageos.org/devices/t6/build
RUN apt-get update \
    && apt-get install -y \
    bc \
    bison \
    build-essential \
    curl \
    flex \
    g++-multilib \
    gcc-multilib \
    git \
    gnupg \
    gperf \
    imagemagick \
    lib32ncurses5-dev \
    lib32readline-dev \
    lib32z1-dev \
    libesd0-dev \
    liblz4-tool \
    libncurses5-dev \
    libsdl1.2-dev \
    libssl-dev \
    libwxgtk3.0-dev \
    libxml2 \
    libxml2-utils \
    lzop \
    pngcrush \
    rsync \
    schedtool \
    squashfs-tools \
    xsltproc \
    zip \
    zlib1g-dev

