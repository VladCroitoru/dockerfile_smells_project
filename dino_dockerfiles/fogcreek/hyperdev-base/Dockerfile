FROM ubuntu:xenial

ENV DPKG_FRONTEND noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# set language
ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

RUN apt-get -y update && apt-get -y install \
    apt-utils \
    locales \
    wget \
    && apt-get -y autoremove && apt-get clean autoclean && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    echo LANG=en_US.UTF-8      > /etc/default/locale && \
    echo LC_MESSAGES=POSIX    >> /etc/default/locale && \
    echo LC_ALL=en_US.UTF-8   >> /etc/environment && \
    echo LANGUAGE=en_US.UTF-8 >> /etc/environment

# Erlang and elixir repositories
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \
    dpkg -i erlang-solutions_1.0_all.deb && \
    rm erlang-solutions_1.0_all.deb

# APL
RUN wget ftp://ftp.gnu.org/gnu/apl/apl_1.6-1_amd64.deb 2>&1 && \
    dpkg -i apl_1.6-1_amd64.deb 2>&1 && \
    rm apl_1.6-1_amd64.deb

# .NET Core
RUN echo "deb [arch=amd64] http://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893

# Java variables
RUN echo JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /etc/environment

# Prepare mysql install
RUN echo 'mysql-server mysql-server/root_password password mysql'       | debconf-set-selections && \
    echo 'mysql-server mysql-server/root_password_again password mysql' | debconf-set-selections

# upgrade packages, install deps
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install \
    apache2 \
    autoconf \
    automake \
    binutils \
    bison \
    build-essential \
    bzip2 \
    clang-3.6 \
    composer \
    curl \
    dos2unix \
    dotnet-dev-1.0.0-preview2.1-003177 \
    emacs \
    elixir \
    esl-erlang \
    ffmpeg \
    flex bison \
    g++ \
    gcc \
    git \
    haskell-platform \
    htop \
    imagemagick \
    libmagick++-dev \
    inetutils-ping \
    jq \
    libapache2-mod-php \
    libbison-dev \
    libbz2-dev \
    libc6-dev \
    libcairo2-dev \
    libcurl4-openssl-dev \
    libdjvulibre-dev \
    libedit-dev \
    libexif-dev \
    libexpat1-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    libgcrypt11-dev \
    libgdbm-dev \
    libgif-dev \
    libgnutls28-dev \
    libgpg-error-dev \
    libgraphviz-dev \
    libgssapi-krb5-2 \
    libicu-dev \
    libidn11-dev \
    libjasper-dev \
    libjasper-dev \
    libjbig-dev \
    libjpeg-dev \
    libjpeg8-dev \
    libkrb5-dev \
    liblcms2-dev \
    liblzma-dev \
    libmysqlclient-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libopenexr-dev \
    libp11-kit-dev \
    libpango1.0-dev \
    libpcre3-dev \
    libpng12-dev \
    libpq-dev \
    libreadline-dev \
    librsvg2-dev \
    librtmp-dev \
    libsqlite0-dev \
    libsqlite3-dev \
    libssl-dev \
    libtcl8.6 \
    libtiff5-dev \
    libtk8.6 \
    libtool-bin \
    libxml2-dev \
    libzmq3-dev \
    linux-libc-dev \
    llvm-dev \
    lua5.2 \
    make \
    maven \
    mongodb \
    mysql-server \
    nano \
    net-tools \
    ocaml \
    openjdk-8-jdk \
    patch \
    php \
    php-mbstring \
    php-mysqli \
    php-xml \
    php-zip \
    pkg-config \
    python \
    python-dev \
    python-pip \
    python3-pip \
    python3-dev \
    rsync \
    ruby \
    ruby-dev \
    runit \
    sqlite \
    subversion \
    telnet \
    vim \
    wget \
    zlib1g-dev \
    && apt-get -y autoremove && apt-get clean autoclean && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.6 100 && \
    update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.6 100

# install dumb-init to manage signal forwarding from the run scripts to the processes they call
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb && \
    dpkg -i dumb-init_*.deb && \
    rm dumb-init_*.deb

# go
RUN wget https://storage.googleapis.com/golang/go1.7.5.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.7.5.linux-amd64.tar.gz && \
    rm go1.7.5.linux-amd64.tar.gz
ENV PATH /usr/local/go/bin:$PATH

# rust
RUN wget https://static.rust-lang.org/rustup.sh && \
    sh rustup.sh --disable-sudo --yes && \
    rm rustup.sh

# update pip
RUN pip3 install --upgrade pip && \
    pip2 install --upgrade pip

# Swift and Vapor
ENV SWIFT_BRANCH swift-3.0.1-release
ENV SWIFT_VERSION swift-3.0.1-RELEASE
ENV SWIFT_PLATFORM ubuntu16.04
COPY swift-keys.asc /tmp/swift-keys.asc
RUN gpg --import /tmp/swift-keys.asc && \
    SWIFT_ARCHIVE_NAME=$SWIFT_VERSION-$SWIFT_PLATFORM && \
    SWIFT_URL=https://swift.org/builds/$SWIFT_BRANCH/$(echo "$SWIFT_PLATFORM" | tr -d .)/$SWIFT_VERSION/$SWIFT_ARCHIVE_NAME.tar.gz && \
    wget $SWIFT_URL && \
    wget $SWIFT_URL.sig && \
    gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \
    tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / --strip-components=1 && \
    rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/* && \
    chmod o+r -R /usr/lib/swift /usr/lib/swift_static && \
    curl -sL toolbox.vapor.sh | bash

# Ponylang
RUN wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre2-10.21.tar.bz2 && \
    tar xvf pcre2-10.21.tar.bz2 && \
    rm pcre2-10.21.tar.bz2 && \
    cd pcre2-10.21 && \
    ./configure --prefix=/usr && \
    make && make install && \
    cd / && \
    git clone git://github.com/ponylang/ponyc && \
    cd ponyc && \
    git checkout 0.10.0 && \
    make && make install && \
    cd / && rm -rf ponyc

# Symfony
RUN curl -LsS https://symfony.com/installer -o /usr/bin/symfony && chmod a+x /usr/bin/symfony

# Rails
RUN gem install rails

# Add nvm to all login shells
RUN echo 'export NVM_DIR="/home/nvm/.nvm"' > /etc/profile.d/nvm.sh
RUN echo 'source ${NVM_DIR}/nvm.sh' >> /etc/profile.d/nvm.sh

# add user for running your apps
RUN adduser --quiet --shell /bin/bash --disabled-password --disabled-login --gecos "" --no-create-home --home /app app

# add user to install nvm
RUN adduser --quiet --shell /bin/bash --disabled-password --disabled-login --gecos "" --home /home/nvm nvm

COPY install-node.sh /tmp/install-node.sh
RUN chown nvm /usr/bin
USER nvm
RUN /tmp/install-node.sh
USER root
