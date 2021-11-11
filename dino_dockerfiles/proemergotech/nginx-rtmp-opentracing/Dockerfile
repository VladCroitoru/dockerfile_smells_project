FROM nvidia/cuda:9.2-devel-ubuntu16.04 AS builder
MAINTAINER Norbert Csibra <norbert.csibra@proemergotech.com>

ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,video

ENV OPENRESTY_VERSION 1.13.6.1
ENV NGINX_RTMP_MODULE_VERSION 1.2.1
ENV NGINX_OPENTRACING_MODULE_VERSION 0.6.0
ENV OPENTRACING_VERSION 1.5.0
ENV FFMPEG_VERSION 4.1
ENV NV_CODEC_HEADERS_VERSION 8.2.15.6

ENV OPENRESTY openresty-${OPENRESTY_VERSION}
ENV NGINX_RTMP_MODULE nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}
ENV NGINX_OPENTRACING_MODULE nginx-opentracing-${NGINX_OPENTRACING_MODULE_VERSION}
ENV OPENTRACING opentracing-cpp-${OPENTRACING_VERSION}

# Common build tools
ENV BUILD_DEPS_OPENRESTY="libpcre3-dev libssl-dev perl make cmake build-essential wget"

# FFMPEG dependencies
ENV BUILD_DEPS_FFMPEG "autoconf automake build-essential cmake git-core libass-dev libfdk-aac-dev libfreetype6-dev libgnutls-dev libmp3lame-dev libopus-dev librtmp-dev libsdl2-dev libtheora-dev libtool libc6 libc6-dev unzip libv4l-dev libvdpau-dev libvorbis-dev libvpx-dev libwebp-dev libx264-dev libx265-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev libxvidcore-dev nasm yasm pkg-config texinfo wget zlib1g-dev libnuma1 libnuma-dev"

# Update packages and install package creator
RUN apt-get update && apt-get install -y checkinstall && mkdir /tmp/packages

# Build Opentracing cpp lib.
RUN set -x \
  && apt-get install -y --no-install-recommends --no-install-suggests ${BUILD_DEPS_OPENRESTY} \
  && cd /tmp \
  && wget https://github.com/opentracing/opentracing-cpp/archive/v${OPENTRACING_VERSION}.tar.gz -O ${OPENTRACING}.tar.gz \
  && tar zxf ${OPENTRACING}.tar.gz \
  && cd ${OPENTRACING} \
  && mkdir .build && cd .build \
  && cmake -DCMAKE_BUILD_TYPE=Release \
           -DBUILD_TESTING=OFF .. \
  && make \
  && checkinstall \
  		--default \
  		--install=no \
  		--nodoc \
  		--pakdir=/tmp/packages \
  		--pkgname=opentracing-cpp \
  		--pkgversion=$OPENTRACING_VERSION \
  		--type=debian \
  			make install

# Get nginx-rtmp.
RUN cd /tmp \
  && wget https://github.com/arut/nginx-rtmp-module/archive/v${NGINX_RTMP_MODULE_VERSION}.tar.gz -O ${NGINX_RTMP_MODULE}.tar.gz \
  && tar zxf ${NGINX_RTMP_MODULE}.tar.gz

# Get nginx-opentracing.
RUN cd /tmp \
  && wget https://github.com/opentracing-contrib/nginx-opentracing/archive/v${NGINX_OPENTRACING_MODULE_VERSION}.tar.gz -O ${NGINX_OPENTRACING_MODULE}.tar.gz \
  && tar zxf ${NGINX_OPENTRACING_MODULE}.tar.gz

# Install openresty, it contains nginx
# and lua, all of the nginx configure
# options are usable.
RUN cd /tmp \
  && wget http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz -O ${OPENRESTY}.tar.gz \
  && tar zxf ${OPENRESTY}.tar.gz \
  && cd ${OPENRESTY} \
  && ./configure \
    --add-dynamic-module=/tmp/${NGINX_OPENTRACING_MODULE}/opentracing \
    --add-module=/tmp/${NGINX_RTMP_MODULE} \
    --with-http_auth_request_module \
    --without-http_echo_module \
    --without-http_xss_module \
    --without-http_coolkit_module \
    --without-http_set_misc_module \
    --without-http_form_input_module \
    --without-http_encrypted_session_module \
    --without-http_srcache_module \
    --without-http_lua_upstream_module \
    --without-http_headers_more_module \
    --without-http_array_var_module \
    --without-http_memc_module \
    --without-http_redis2_module \
    --without-http_redis_module \
    --without-http_rds_json_module \
    --without-http_rds_csv_module \
    --without-stream_lua_module \
    --without-http_ssl_module \
    --without-lua_cjson \
    --without-lua_redis_parser \
    --without-lua_rds_parser \
    --without-lua_resty_dns \
    --without-lua_resty_memcached \
    --without-lua_resty_redis \
    --without-lua_resty_mysql \
    --without-lua_resty_upload \
    --without-lua_resty_upstream_healthcheck \
    --without-lua_resty_string \
    --without-lua_resty_websocket \
    --without-lua_resty_limit_traffic \
    --without-lua_resty_lock \
    --without-lua_resty_lrucache \
    --without-mail_pop3_module \
    --without-mail_imap_module \
    --without-mail_smtp_module \
    --with-pcre \
    --with-debug \
    --with-compat \
    --with-luajit \
    --user=nginx \
    --group=nginx \
  && make \
  && checkinstall \
      --default \
      --install=no \
      --nodoc \
      --pakdir=/tmp/packages \
      --pkgname=openresty \
      --pkgversion=$OPENRESTY_VERSION \
      --type=debian \
        make install

# Installing Nvidia codec headers
# The NVIDIA headers were moved out of the FFmpeg codebase to a standalone repository in commit 27cbbbb.
# From the commit message:
# External headers are no longer welcome in the ffmpeg codebase because they increase the maintenance burden.
# However, in the NVidia case the vanilla headers need some modifications to be usable in ffmpeg
# therefore we still provide them, but in a separate repository.
RUN cd /tmp \
  && wget https://github.com/FFmpeg/nv-codec-headers/releases/download/n${NV_CODEC_HEADERS_VERSION}/nv-codec-headers-${NV_CODEC_HEADERS_VERSION}.tar.gz \
  && tar zxf nv-codec-headers-${NV_CODEC_HEADERS_VERSION}.tar.gz \
  && cd nv-codec-headers-n${NV_CODEC_HEADERS_VERSION} \
  && make install

# Installing ffmpeg
RUN set -x \
  && apt-get install -y --no-install-recommends --no-install-suggests ${BUILD_DEPS_FFMPEG} \
  && cd /tmp/ \
  && wget http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz \
  && tar zxf ffmpeg-${FFMPEG_VERSION}.tar.gz \
  && cd /tmp/ffmpeg-${FFMPEG_VERSION} \
  && ./configure \
    --enable-version3 \
    --enable-gpl \
    --enable-nonfree \
    --enable-small \
    --enable-libmp3lame \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libvpx \
    --enable-libtheora \
    --enable-libvorbis \
    --enable-libopus \
    --enable-libfdk-aac \
    --enable-libass \
    --enable-libwebp \
    --enable-librtmp \
    --enable-postproc \
    --enable-avresample \
    --enable-libfreetype \
    --enable-gnutls \
    --enable-avfilter \
    --enable-libxvid \
    --enable-libv4l2 \
    --enable-pic \
    --enable-shared \
    --enable-pthreads \
    --enable-shared \
    --enable-nvenc \
    --enable-cuda \
    --enable-cuvid \
    --enable-libnpp \
    --disable-stripping \
    --disable-static \
    --disable-debug \
    --extra-cflags=-I/usr/local/cuda/include \
    --extra-ldflags=-L/usr/local/cuda/lib64 \
  && make \
  && checkinstall \
      --default \
      --install=no \
      --nodoc \
      --pakdir=/tmp/packages \
      --pkgname=ffmpeg \
      --pkgversion=$FFMPEG_VERSION \
      --type=debian \
        make install


FROM nvidia/cuda:9.2-runtime-ubuntu16.04

ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,video

ENV JAEGER_VERSION 0.4.2

# Installing runtime dependencies and helpers
RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests wget libxv1 x264 x265 libsdl2-2.0-0 libv4l-0 libxcb-shm0 libxcb-shape0 libass5 libfdk-aac0 libvdpau1

# Add Jaeger tracing dynamic plugin
RUN wget https://github.com/jaegertracing/jaeger-client-cpp/releases/download/v${JAEGER_VERSION}/libjaegertracing_plugin.linux_amd64.so -O /usr/local/lib/libjaegertracing_plugin.so

COPY --from=builder /tmp/packages /tmp/packages

RUN dpkg -i /tmp/packages/*.deb

# Add openresty bins to PATH
ENV PATH=$PATH:/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin

# base image overwrite this env and ffmpeg install shared libraries to /usr/local/lib, so we need to add
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/lib"

# Adding nginx configuration file
ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

# Prepare data directory
RUN mkdir -p /data \
  && mkdir -p /data/hls \
  && mkdir -p /data/dash \
  && mkdir -p /www

# Add necessary user and group
RUN addgroup --system nginx \
  && adduser --system --disabled-password --home /var/cache/nginx --shell /sbin/nologin --ingroup nginx nginx

# Add static files
ADD static /www/static

# Expose RTMP port
EXPOSE 1935

# Expose HTTP port
EXPOSE 80

# Start NGINX
CMD ["/usr/local/openresty/nginx/sbin/nginx"]


