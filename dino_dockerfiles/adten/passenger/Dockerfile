## Using Alpine Linux results in a much smaller image than using say Ubuntu
FROM adten/ruby:2.1.6
MAINTAINER John Axel Eriksson <john.eriksson@playad.se>

ENV \
  PASSENGER=passenger-5.0.21 \
  NGINX=1.9.4 \
  PATH="/passenger/bin:/opt/nginx/sbin:$PATH" \
  TINI_VERSION=v0.8.3 \
  TERM=xterm-color \
  ERROR_LOG=/dev/stdout \
  ACCESS_LOG=/dev/stdout

# Add tini (a tiny init process)
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /tini

# install build deps
RUN chmod +x /tini \
 && apk add --update procps pcre libstdc++ \
 && apk add openssl-dev build-base linux-headers curl-dev pcre-dev \
 && apk add --update-cache --repository 'http://nl.alpinelinux.org/alpine/edge/testing' libexecinfo libexecinfo-dev \
 && wget "https://s3.amazonaws.com/phusion-passenger/releases/$PASSENGER.tar.gz" \
 && tar xzf "$PASSENGER.tar.gz" && rm "$PASSENGER.tar.gz" \
 && mv "$PASSENGER" /passenger && cd /passenger \
 && export EXTRA_PRE_CFLAGS='-O' EXTRA_PRE_CXXFLAGS='-O' EXTRA_LDFLAGS='-lexecinfo' \
 && rm -rf /tmp/* /passenger/doc \
 && wget "http://nginx.org/download/nginx-$NGINX.tar.gz" \
 && tar xzf "nginx-$NGINX.tar.gz" && rm "nginx-$NGINX.tar.gz" \
 && mv "nginx-$NGINX" /nginx && cd /nginx \
 && readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
 && ./configure --prefix=/opt/nginx --add-module=$(passenger-config --nginx-addon-dir) --with-pcre-jit --with-ipv6 --without-http_fastcgi_module --without-http_scgi_module --without-http_uwsgi_module --with-http_ssl_module \
 && make -j${NPROC} && make install \
 && apk del wget build-base linux-headers curl-dev pcre-dev libexecinfo-dev || true \
 && rm -rf /var/cache/apk/* /nginx \
 && passenger-config validate-install --auto

# Set the entrypoint script. This should be set again in Dockerfiles depending on this image.
ENTRYPOINT ["/tini", "--"]
