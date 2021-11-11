FROM node:7

RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list \
    && echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list \
    && wget https://www.dotdeb.org/dotdeb.gpg \
    && apt-key add dotdeb.gpg \
    && apt-get update && apt-get install -yqq --no-install-recommends \
        php7.0 php7.0-mbstring \
    && apt-get clean autoclean && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY gitconfig /etc/gitconfig
