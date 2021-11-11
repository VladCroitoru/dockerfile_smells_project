FROM php:5.6-alpine

MAINTAINER erwinmaruli <erwinmaruli@live.com>

WORKDIR /usr/src/app

#Add additional config
COPY config/cust.ini /usr/local/etc/php/conf.d/

# we need to update repo database
RUN apk update && apk upgrade --update &&\
#in some case php composer need git to download dependency
#alpine by default come with ash shell so that we install bash
#in case we need specific bash commands or scripts
    apk add --no-cache bash openssh git &&\
#install pdo_mysql
    docker-php-ext-install pdo_mysql &&\
#install gd
    apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev\
    libjpeg-turbo-dev && docker-php-ext-configure gd\
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ && \
    NPROC=$(getconf _NPROCESSORS_ONLN) && \
    docker-php-ext-install -j${NPROC} gd && \
    apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev && \
#install mcrypt
    apk add --no-cache libmcrypt-dev libltdl && \
    docker-php-ext-configure mcrypt && \
    docker-php-ext-install mcrypt && \

#install composer
    curl -o /usr/local/bin/composer.phar https://getcomposer.org/composer.phar && \
    ln -s /usr/local/bin/composer.phar /usr/local/bin/composer && \
    chmod 755 /usr/local/bin/composer* && \
    echo "<?php phpinfo(); ?>" > index.php && \

#grant execute permission for custom config
    chmod 755 /usr/local/etc/php/conf.d/cust.ini

# Java Version and other ENV
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=121 \
    JAVA_VERSION_BUILD=13 \
    JAVA_PACKAGE=jdk \
    JAVA_JCE=standard \
    JAVA_HOME=/opt/jdk \
    PATH=${PATH}:/opt/jdk/bin \
    GLIBC_VERSION=2.23-r3 \
    LANG=C.UTF-8

# do all in one step
RUN set -ex && \
    apk add --update libstdc++ curl ca-certificates bash && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    mkdir /opt && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/java.tar.gz \
    http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/e9e7ea248e2c4826b92b3f075a80e441/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz && \
    gunzip /tmp/java.tar.gz && \
    tar -C /opt -xf /tmp/java.tar && \
    ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \
    if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE policy" >&2 && \
        curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \
            http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip && \
        cd /tmp && unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \
        cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/jdk/jre/lib/security; \
    fi && \
    sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/ $JAVA_HOME/jre/lib/security/java.security && \
    apk del curl glibc-i18n && \
    rm -rf /opt/jdk/*src.zip \
        /opt/jdk/lib/missioncontrol \
        /opt/jdk/lib/visualvm \
        /opt/jdk/lib/*javafx* \
        /opt/jdk/jre/plugin \
        /opt/jdk/jre/bin/javaws \
        /opt/jdk/jre/bin/jjs \
        /opt/jdk/jre/bin/orbd \
        /opt/jdk/jre/bin/pack200 \
        /opt/jdk/jre/bin/policytool \
        /opt/jdk/jre/bin/rmid \
        /opt/jdk/jre/bin/rmiregistry \
        /opt/jdk/jre/bin/servertool \
        /opt/jdk/jre/bin/tnameserv \
        /opt/jdk/jre/bin/unpack200 \
        /opt/jdk/jre/lib/javaws.jar \
        /opt/jdk/jre/lib/deploy* \
        /opt/jdk/jre/lib/desktop \
        /opt/jdk/jre/lib/*javafx* \
        /opt/jdk/jre/lib/*jfx* \
        /opt/jdk/jre/lib/amd64/libdecora_sse.so \
        /opt/jdk/jre/lib/amd64/libprism_*.so \
        /opt/jdk/jre/lib/amd64/libfxplugins.so \
        /opt/jdk/jre/lib/amd64/libglass.so \
        /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
        /opt/jdk/jre/lib/amd64/libjavafx*.so \
        /opt/jdk/jre/lib/amd64/libjfx*.so \
        /opt/jdk/jre/lib/ext/jfxrt.jar \
        /opt/jdk/jre/lib/ext/nashorn.jar \
        /opt/jdk/jre/lib/oblique-fonts \
        /opt/jdk/jre/lib/plugin.jar \
        /tmp/* /var/cache/apk/* && \
        echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

# Start the app
ENTRYPOINT ["php"]
CMD ["-v"]
