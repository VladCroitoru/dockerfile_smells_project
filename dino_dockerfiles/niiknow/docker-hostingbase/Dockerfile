FROM phusion/baseimage:0.10.2
LABEL maintainer="noogen <friends@niiknow.org>"
ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 TERM=xterm container=docker
ENV V8VER=7.5
COPY rootfs/. /
RUN cd /tmp \
    && chmod +x /etc/service/sshd/run \
    && chmod +x /usr/bin/backup-creds.sh \
    && chmod +x /etc/service/incrond/run \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \
    && curl -L https://packages.couchbase.com/clients/c/repos/deb/couchbase.key | apt-key add - \
    && echo "deb https://packages.couchbase.com/clients/c/repos/deb/ubuntu1604 xenial xenial/main" > /etc/apt/sources.list.d/couchbase.list \
    && add-apt-repository -y ppa:couchdb/stable \
    && apt-add-repository -y ppa:ondrej/php \
    && add-apt-repository -y ppa:stesie/libv8 \
    && apt-get update && apt-get -yf -o Dpkg::Options::="--force-confdef" --no-install-recommends upgrade \
    && apt-get -y --no-install-recommends --allow-unauthenticated install wget curl unzip nano vim rsync apt-transport-https openssh-client openssh-server \
       sudo tar git apt-utils software-properties-common build-essential python-dev tcl openssl libpcre3 dnsmasq ca-certificates libpcre3-dev re2c \
       libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev libmagickwand-dev procps imagemagick netcat pkg-config \
       mcrypt pwgen language-pack-en-base libicu-dev g++ cpp libglib2.0-dev incron libcouchbase3 libcouchbase-dev libcouchbase3-tools libcouchbase-dbg libcouchbase3-libev libcouchbase3-libevent \
       libc6 libcurl3 libgcc1 libgssapi-krb5-2 liblttng-ust0 libssl1.0.0 libstdc++6 libunwind8 libuuid1 zlib1g libasan2 libv8-$V8VER-dev \
       php-pear php-xml php7.3-dev php7.3-xml php7.4-dev php7.4-xml php8.0-dev php8.0-xml \
    && systemctl disable incron \
    && echo 'root' >> /etc/incron.allow \
    && dpkg --configure -a \
    && pecl channel-update pecl.php.net \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /core \
    && ls -la /usr/lib/php
RUN /usr/bin/switch-php.sh "8.0" \
    && pecl -d php_suffix=8.0 install -f --alldeps igbinary \
    && mkdir -p /mytmp/20200930 && rsync -ahp /usr/lib/php/20200930/ /mytmp/20200930/ \
    && rm -rf /tmp/*
RUN /usr/bin/switch-php.sh "7.4" \
    && pecl -d php_suffix=7.4 install -f --alldeps pcs igbinary couchbase imagick \
    && git clone https://github.com/phpv8/v8js.git /tmp/v8js \
    && cd /tmp/v8js \
    && git checkout php7 && phpize7.4 \
    && sed -i -e '132s/retval/object/g' v8js_v8object_class.cc \
    && ./configure --with-v8js=/opt/libv8-$V8VER/ LDFLAGS="-lstdc++" \
    && make all test install \
    && mkdir -p /mytmp/20190902 && rsync -ahp /usr/lib/php/20190902/ /mytmp/20190902/ \
    && rm -rf /tmp/*
RUN /usr/bin/switch-php.sh "7.3" \
    && pecl -d php_suffix=7.3 install -f --alldeps pcs igbinary couchbase imagick \
    && git clone https://github.com/phpv8/v8js.git /tmp/v8js \
    && cd /tmp/v8js \
    && git checkout php7 && phpize7.3 \
    && ./configure --with-v8js=/opt/libv8-$V8VER/ LDFLAGS="-lstdc++" \
    && make all test install \
    && rsync -ahp /mytmp/20200930/ /usr/lib/php/20200930/ \
    && rsync -ahp /mytmp/20190902/ /usr/lib/php/20190902/ \
    && rm -rf /mytmp \
    && rm -rf /tmp/*
RUN curl -s -o /tmp/python-support_1.0.15_all.deb https://launchpadlibrarian.net/109052632/python-support_1.0.15_all.deb \
    && dpkg -i /tmp/python-support_1.0.15_all.deb \
    && apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 \
    && add-apt-repository 'deb [arch=amd64,i386] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main' \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 91FA4AD5 \
    && echo 'deb [arch=amd64,i386] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse' \
        | sudo tee /etc/apt/sources.list.d/mongodb-3.6.list \
    && apt-get update && apt-get -y --no-install-recommends upgrade \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /core \
    && rm -rf /tmp/* \
    && find /etc/service/ -name "down" -exec rm -f {} \; 

ENV DEBIAN_FRONTEND=teletype

VOLUME ["/backup"]

CMD ["/sbin/my_init"]
