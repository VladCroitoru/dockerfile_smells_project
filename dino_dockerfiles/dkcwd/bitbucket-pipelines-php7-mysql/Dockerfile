FROM dkcwd/bitbucket-pipelines-default:latest
MAINTAINER Dave Clark "dave.clark@clarkyoungman.com"

# Handle apt pub key updates
COPY pubkey_0x4f4ea0aae5267a6c /tmp/pubkey_0x4f4ea0aae5267a6c
RUN DEBIAN_FRONTEND=noninteractive apt-key add /tmp/pubkey_0x4f4ea0aae5267a6c

# Dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-key update && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    software-properties-common \
    python-software-properties \
    build-essential \
    curl \
    git \
    unzip \
    mcrypt \
    wget \
    openssl \
    autoconf \
    g++ \
    make \
    libssl-dev \
    libcurl4-openssl-dev \
    libsasl2-dev \
    libcurl3 \
    --no-install-recommends && rm -r /var/lib/apt/lists/* \
    && apt-get --purge autoremove -y

RUN DEBIAN_FRONTEND=noninteractive apt-get update

RUN mkdir -p /usr/local/openssl/include/openssl/ && \
    ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \
    mkdir -p /usr/local/openssl/lib/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/

# MySQL
ARG MYSQL_ROOT_PASS=root 
RUN bash -c 'debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASS"' && \
		bash -c 'debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASS"' && \
		DEBIAN_FRONTEND=noninteractive apt-get update && \
		DEBIAN_FRONTEND=noninteractive apt-get install -qqy mysql-server
		
# PHP7
RUN add-apt-repository -y ppa:ondrej/php && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y -qq php-pear php7.0-dev php7.0-fpm php7.0-mcrypt php7.0-zip php7.0-xml php7.0-mbstring php7.0-curl php7.0-json php7.0-mysql php7.0-tokenizer php7.0-cli php7.0-imap php7.0-soap && \
    apt-get remove --purge php5 php5-common

RUN service php7.0-fpm restart

# PhantomJS
COPY install-phantomjs.sh /tmp/install-phantomjs.sh
RUN sh /tmp/install-phantomjs.sh
COPY phantomjs /etc/init.d/phantomjs
RUN echo 'WEBDRIVER_PORT=8190' > /etc/default/phantomjs
RUN chmod +x /etc/init.d/phantomjs
RUN update-rc.d phantomjs defaults
RUN service phantomjs start

RUN apt-get clean && \
		apt-get autoremove && \
		rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80 8000 8080 8190 6379 443 4444 3306
