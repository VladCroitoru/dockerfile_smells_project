FROM node:11.6.0-alpine

COPY docker-entrypoint.sh /opt/docker-entrypoint.sh

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN echo  >> /etc/apk/repositories && \
    apk add --no-cache \
            bash \
            wget \
            gzip \
            exiftool \
            fbida-exiftran \
            jpegoptim@testing \
            pngquant@testing \
            imagemagick \
            optipng && \
    mkdir -p /u/ && \
    mkdir -p /opt/npm/ && \
    mkdir -p /opt/node/ && \
    mkdir -p /opt/npm/uploads && \
    mkdir -p /opt/npm/app && \
    addgroup -g 10777 nodeworker && \
    adduser -D -G nodeworker -u 10777 nodeworker && \
    chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint.sh && \
    chown -R nodeworker:nodeworker /opt/npm && \
    chown -R nodeworker:nodeworker /u



#
# MAKE optipng 0.7.6 with my "awesome-STDOUT-patch",
# so that only errors are logged to STDERR
# and normal output is logged to STDOUT
#
RUN apk add --no-cache --virtual .build-deps \
            libstdc++ \
            binutils-gold \
            curl \
            g++ \
            gcc \
            gnupg \
            libgcc \
            linux-headers \
            make \
            git
RUN mkdir -p /opt/optipng-build/ && \
    wget -O /opt/optipng-0.7.6.zip https://codeclou.github.io/kartoffelstampf/repo/optipng-0.7.6-patched.zip && \
    unzip /opt/optipng-0.7.6.zip -d /opt/optipng-build/ && \
    cd /opt/optipng-build/optipng-0.7.6/ && \
    ./configure  && \
    make  && \
    make install  && \
    rm -rf /opt/optipng-build/



#
# GLFAGS https://github.com/gflags/gflags
#
RUN apk add --no-cache --virtual .build-deps-gflags cmake && \
    mkdir -p /opt/build/gflags/gflags-2.2.0 && \
    wget -O /opt/build/gflags/gflags-2.2.0.zip https://codeclou.github.io/kartoffelstampf/repo/gflags-2.2.0-pre-configured-cmake.zip && \
    unzip /opt/build/gflags/gflags-2.2.0.zip -d /opt/build/gflags/gflags-2.2.0 && \
    cd /opt/build/gflags/gflags-2.2.0 && \
    # NOTE: we already did CMAKE manually and zipped the result
    #       also did we manually download the git-submodule dir /doc and inject it in our zip
    make && \
    make install && \
    rm -rf /opt/build/gflags/

#
# GUETZLI https://github.com/google/guetzli
#
# @DependsOn GFLAGS
#
RUN apk add --no-cache --virtual .build-deps-guetzli libpng libpng-dev && \
    mkdir -p /opt/build/guetzli/guetzli-1.0 && \
    wget -O /opt/build/guetzli/guetzli-1.0.zip https://github.com/google/guetzli/archive/v1.0.zip && \
    unzip /opt/build/guetzli/guetzli-1.0.zip -d /opt/build/guetzli/guetzli-1.0 && \
    cd /opt/build/guetzli/guetzli-1.0/guetzli-1.0 && \
    make && \
    mv /opt/build/guetzli/guetzli-1.0/guetzli-1.0/bin/Release/guetzli /usr/local/bin && \
    rm -rf /opt/build/guetzli/

#
# INSTALL KARTOFFELSTAMP-SERVER AND CLIENT
#
USER nodeworker
ENV KARTOFFELSTAMPF_SERVER_VERSION v2.3.0
ENV KARTOFFELSTAMPF_CLIENT_VERSION v2.3.0
RUN wget -O /opt/npm/kartoffelstampf-server.zip https://github.com/codeclou/kartoffelstampf-server/releases/download/${KARTOFFELSTAMPF_SERVER_VERSION}/dist.zip && \
    unzip /opt/npm/kartoffelstampf-server.zip -d /opt/npm/app/ && \
    rm -f /opt/npm/kartoffelstampf-server.zip  && \
    ls -lah /opt/npm/app/ && \
    mkdir /opt/npm/public/ && \
    wget -O /opt/npm/kartoffelstampf-client.zip https://github.com/codeclou/kartoffelstampf-client/releases/download/${KARTOFFELSTAMPF_CLIENT_VERSION}/dist.zip && \
    unzip /opt/npm/kartoffelstampf-client.zip -d /opt/npm/public/ && \
    rm -f /opt/npm/kartoffelstampf-client.zip  && \
    ls -lah /opt/npm/public/ && \
    cd /opt/npm/app/ && npm install && npm prune --production

#
# RUN
#
EXPOSE 9999
VOLUME ["/opt/npm/app/"]
VOLUME ["/u"]
WORKDIR /opt/npm/app/
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
CMD ["npm", "run", "start:prod"]