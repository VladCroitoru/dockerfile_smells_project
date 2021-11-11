FROM debian:buster-slim

# Stop apt-get asking to get Dialog frontend
ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm

# LinuxGSM_ variables
ENV LGSM_VERSION="latest" \
    LGSM_GAMESERVER="" \
    LGSM_GAMESERVER_UPDATE="true" \
    LGSM_GAMESERVER_START="false" \
    LGSM_GAMESERVER_RENAME="" \
    LGSM_COMMON_CONFIG="" \
    LGSM_COMMON_CONFIG_FILE="" \
    LGSM_SERVER_CONFIG="" \
    LGSM_SERVER_CONFIG_FILE=""

# Fix for JRE installation
RUN mkdir -p /usr/share/man/man1/

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
        bc \
        binutils \
        bsdmainutils \
        bzip2 \
        ca-certificates \
        curl \
        default-jre \
        file \
        gzip \
        iproute2 \
        jq \
        lib32gcc1 \
        lib32stdc++6 \
        libsdl2-2.0-0:i386 \
        locales \
        mailutils \
        netcat \
        nodejs \
        postfix \
        procps \
        python \
        tar \
        tmux \
        util-linux \
        unzip \
        wget && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
        nodejs && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*

RUN npm set progress=false && \
    npm config set depth 0 && \
    npm install --no-audit --global gamedig && \
    npm cache clean --force

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \ 
    LC_ALL=en_US.UTF-8

# Add the steam user
RUN adduser \
    --disabled-login \
    --disabled-password \
    --shell /bin/bash \
    --gecos "" \
    linuxgsm && \
    usermod -G tty linuxgsm

COPY ./scripts/*.sh /
RUN chmod +x /*.sh

# Switch to the user steam
USER linuxgsm
WORKDIR /home/linuxgsm

ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK --interval=60s --timeout=30s --start-period=300s --retries=3 CMD [ "/lgsm_healthcheck.sh" ]
