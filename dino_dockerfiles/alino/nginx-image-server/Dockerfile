FROM quay.io/wantedly/buildpack-deps:14.04
MAINTAINER Seigo Uchida <spesnova@gmail.com> (@spesnova)

ENV NGINX_VERSION 1.6.2
ENV NGX_SMALL_LIGHT_VERSION 0.6.8
ENV IMAGEMAGICK_VERSION 6.8.6-8

# Install dependency packages
RUN apt-get update && \
    apt-get install -y \
      binutils-doc \
      bison \
      flex \
      gettext \
      libpcre3 \
      libpcre3-dev \
      libssl-dev \
      wget \
      vim \
      libperl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install nodejs
RUN apt-get install git && \
    cd /tmp && \
    wget https://nodejs.org/dist/v4.2.3/node-v4.2.3-linux-x64.tar.gz && \
    mkdir /node && \
    tar xvf node-v*.tar.?z --strip-components=1 -C /node && \
    mkdir /node/etc && \
    echo 'prefix=/usr/local' > /node/etc/npmrc && \
    mv /node /opt/ && \
    chown -R root: /opt/node && \
    ln -s /opt/node/bin/node /usr/local/bin/node && \
    ln -s /opt/node/bin/npm /usr/local/bin/npm && \
    node -v

# Install forever
RUN npm install forever -g

# Install npm deps
RUN mkdir nodeApp && \
    cd /nodeApp && \
    npm install express && \
    npm install body-parser && \
    npm install mkdirp && \
    npm install path

# Build ImageMagick with WebP support
RUN mkdir -p /tmp/imagemagick && \
    cd /tmp/imagemagick && \
    apt-get update && \
    apt-get build-dep -y imagemagick && \
    apt-get install -y libwebp-dev devscripts checkinstall && \
    curl -L https://launchpad.net/imagemagick/main/${IMAGEMAGICK_VERSION}/+download/ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz > \
      ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz && \
    tar zxf ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz && \
    cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    ./configure \
      --prefix=/usr \
      --sysconfdir=/etc \
      --libdir=/usr/lib/x86_64-linux-gnu \
      --enable-shared \
      --with-modules \
      --disable-openmp \
      --with-webp=yes \
      LDFLAGS=-L/usr/local/lib \
      CPPFLAGS=-I/usr/local/include && \
    make && \
    checkinstall -y && \
    rm -rf /tmp/imagemagick && \
    rm -rf /var/lib/apt/lists/*

# Fetch and unarchive nginx source
RUN curl -L http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz > /tmp/nginx-${NGINX_VERSION}.tar.gz && \
    cd /tmp && \
    tar zxf nginx-${NGINX_VERSION}.tar.gz

# Fetch and unarchive ngx_small_light module
RUN curl -L https://github.com/cubicdaiya/ngx_small_light/archive/v${NGX_SMALL_LIGHT_VERSION}.tar.gz > /tmp/ngx_small_light-${NGX_SMALL_LIGHT_VERSION}.tar.gz && \
    cd /tmp && \
    tar zxf ngx_small_light-${NGX_SMALL_LIGHT_VERSION}.tar.gz && \
    cd /tmp/ngx_small_light-${NGX_SMALL_LIGHT_VERSION} && \
    ./setup

# Fetch and unarchive nginx-upload-module
RUN curl -L https://api.github.com/repos/vkholodkov/nginx-upload-module/tarball/2.2 > /tmp/nginx-upload-module-2.2.0.tar.gz && \
    cd /tmp && \
    tar zxf nginx-upload-module-2.2.0.tar.gz && \
    ls -la /tmp && \
    ls -la /tmp/vkholodkov-nginx-upload-module-aba1e3f && \
    cat /tmp/vkholodkov-nginx-upload-module-aba1e3f/config


# Compile nginx
RUN cd /tmp/nginx-${NGINX_VERSION} && \
    ./configure \
      --prefix=/opt/nginx \
      --conf-path=/etc/nginx/nginx.conf \
      --sbin-path=/opt/nginx/sbin/nginx \
      --with-http_stub_status_module \
      --with-http_perl_module \
      --with-pcre \
      --add-module=/tmp/ngx_small_light-${NGX_SMALL_LIGHT_VERSION} \
      --add-module=/tmp/vkholodkov-nginx-upload-module-aba1e3f && \
    make && \
    make install && \
    rm -rf /tmp/*

RUN mkdir -p /etc/nginx && \
    mkdir -p /opt/nginx/perl/lib && \
    mkdir -p /var/run && \
    mkdir -p /etc/nginx/conf.d && \
    mkdir -p /var/www/nginx/cache && \
    mkdir -p /var/www/nginx/images && \
    mkdir -p /var/www/nginx/tmp

# Add config files
COPY files/nginx.conf   /etc/nginx/nginx.conf
COPY files/mime.types   /etc/nginx/mime.types
COPY files/validator.pm /opt/nginx/perl/lib/validator.pm
COPY files/renameImage.js /nodeApp/renameImage.js
COPY entrypoint.sh /opt/entrypoint.sh

EXPOSE 80 8090

ENTRYPOINT /opt/entrypoint.sh