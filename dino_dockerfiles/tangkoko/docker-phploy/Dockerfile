FROM alpine

RUN apk add --update \
    ca-certificates \
    openssh-client \
    bash \
    git \
    mercurial \
    php-bz2 \
    php-cli \
    php-dom \
    php-gd \
    php-json \
    php-ftp \
    php-mcrypt \
    php-openssl \
    php-pdo \
    php-pear \
    php-phar \
    php-zip \
    php-ctype \
    php-zlib \
    subversion \
    unrar \
    perl \
    && rm -rf /var/cache/apk/*

RUN git clone https://github.com/tangkoko/PHPloy.git && \
	chmod +x PHPloy/dist/phploy.phar && \
    mv PHPloy/dist/phploy.phar /usr/local/bin/phploy

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app
