FROM ubuntu:16.04
MAINTAINER LineageOS Infrastructure Team <infra@lienageos.org>

ENV DEBIAN_FRONTEND noninteractive

# Build tools
RUN apt-get update && apt-get -y --no-install-recommends install \
    openjdk-8-jdk \
    python \
    bc \
    yasm \
    rsync \
    schedtool \
    imagemagick \
    git-core \
    gnupg \
    flex \
    bison \
    gperf \
    build-essential \
    zip \
    curl \
    zlib1g-dev \
    gcc-multilib \
    g++-multilib \
    libc6-dev-i386 \
    lib32ncurses5-dev \
    x11proto-core-dev \
    libx11-dev \
    lib32z-dev \
    ccache \
    libgl1-mesa-dev \
    libxml2-utils \
    xsltproc \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*



# Add tools
ADD https://commondatastorage.googleapis.com/git-repo-downloads/repo /usr/local/bin/
ADD https://jenkins.lineageos.org/jnlpJars/slave.jar /usr/local/bin/
RUN chmod 755 /usr/local/bin/*

# Add s6-overlay
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

# Add user
RUN useradd lineage --home-dir=/opt/lineage && mkdir /opt/lineage

#Add /lineage and /ccache volumes
VOLUME /lineage/
VOLUME /ccache/

COPY /root /

ENTRYPOINT ["/init"]
