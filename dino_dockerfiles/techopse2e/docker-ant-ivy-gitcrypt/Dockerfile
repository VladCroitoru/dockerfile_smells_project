FROM openjdk:jdk-alpine
ENV GIT_CRYPT_VERSION 0.5.0-2
ENV IVY_VERSION 2.4.0
RUN apk add --update \
    apache-ant --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
    --allow-untrusted \
    bash \
    curl \
    git \
    g++ \
    make \
    openssh \
    openssl \
    openssl-dev \
    zip && \
    rm -rf /var/cache/apk/* && \
    curl -o /var/tmp/ivy.zip https://www.apache.org/dist/ant/ivy/$IVY_VERSION/apache-ivy-$IVY_VERSION-bin.zip && \
    unzip /var/tmp/ivy.zip -d /var/tmp && \
    cp /var/tmp/apache-ivy-$IVY_VERSION/ivy-$IVY_VERSION.jar /usr/share/java/apache-ant/lib && \
    curl -L https://github.com/AGWA/git-crypt/archive/debian/$GIT_CRYPT_VERSION.tar.gz | tar zxv -C /var/tmp && \
    cd /var/tmp/git-crypt-debian-$GIT_CRYPT_VERSION && \
    make && make install PREFIX=/usr/local && \
    rm -rf /var/tmp/* && \
    apk del make openssl-dev


ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin
