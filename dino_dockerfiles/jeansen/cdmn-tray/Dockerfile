FROM debian

ENV DEBUG_COLORS true
ENV FORCE_COLOR true
ENV DEBIAN_FRONTEND noninteractive
# ENV DEBUG=electron-builder

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
        apt-transport-https \
        autoconf \
        bsdtar \
        build-essential \
        curl \
        g++-multilib \
        gcc-multilib \
        gnupg \
        graphicsmagick \ 
        icnsutils \
        libcurl3 \
        libgnome-keyring-dev \
        libopenjp2-tools \
        libsecret-1-0 \
        libssl-dev \
        locales \
        lsb-release \
        lzip \
        python \
        qtbase5-dev \
        rpm \
        software-properties-common \
        wget \
        xorriso \
        yasm && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
	apt-get update -y && \
    apt-get --no-install-recommends -y install \
        nodejs \
        google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
locale-gen en_US.UTF-8 && dpkg-reconfigure locales

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
