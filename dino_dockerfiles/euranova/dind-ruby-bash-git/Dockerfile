FROM docker:git

# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
  && { \
    echo 'install: --no-document'; \
    echo 'update: --no-document'; \
  } >> /usr/local/etc/gemrc

ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.2
ENV RUBY_DOWNLOAD_SHA256 748a8980d30141bd1a4124e11745bb105b436fb1890826e0d2b9ea31af27f735
ENV RUBYGEMS_VERSION 2.6.13

# some of ruby's build scripts are written in ruby
#   we purge system ruby later to make sure our final image uses what we just built
# readline-dev vs libedit-dev: https://bugs.ruby-lang.org/issues/11869 and https://github.com/docker-library/ruby/issues/75
RUN set -ex \
  \
  && apk add --no-cache --virtual .ruby-builddeps \
    autoconf \
    bison \
    bzip2 \
    bzip2-dev \
    ca-certificates \
    coreutils \
    dpkg-dev dpkg \
    gcc \
    gdbm-dev \
    glib-dev \
    libc-dev \
    libffi-dev \
    libressl \
    libressl-dev \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    make \
    ncurses-dev \
    procps \
    readline-dev \
    ruby \
    tar \
    xz \
    yaml-dev \
    zlib-dev \
  \
  && wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \
  && echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - \
  \
  && mkdir -p /usr/src/ruby \
  && tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \
  && rm ruby.tar.xz \
  \
  && cd /usr/src/ruby \
  \
# hack in "ENABLE_PATH_CHECK" disabling to suppress:
#   warning: Insecure world writable dir
  && { \
    echo '#define ENABLE_PATH_CHECK 0'; \
    echo; \
    cat file.c; \
  } > file.c.new \
  && mv file.c.new file.c \
  \
  && autoconf \
  && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
# the configure script does not detect isnan/isinf as macros
  && export ac_cv_func_isnan=yes ac_cv_func_isinf=yes \
  && ./configure \
    --build="$gnuArch" \
    --disable-install-doc \
    --enable-shared \
  && make -j "$(nproc)" \
  && make install \
  \
  && runDeps="$( \
    scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
      | tr ',' '\n' \
      | sort -u \
      | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
  )" \
  && apk add --virtual .ruby-rundeps $runDeps \
    bzip2 \
    ca-certificates \
    libffi-dev \
    libressl-dev \
    procps \
    yaml-dev \
    zlib-dev \
  && apk del .ruby-builddeps \
  && cd / \
  && rm -r /usr/src/ruby \
  \
  && gem update --system "$RUBYGEMS_VERSION"

ENV BUNDLER_VERSION 1.15.4

RUN gem install bundler --version "$BUNDLER_VERSION"

# install things globally, for great justice
# and don't create ".bundle" in all our apps
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
  BUNDLE_BIN="$GEM_HOME/bin" \
  BUNDLE_SILENCE_ROOT_WARNING=1 \
  BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"

# gpg: key 64EA74AB: public key "Chet Ramey <chet@cwru.edu>" imported
ENV _BASH_GPG_KEY 7C0135FB088AAF6C66C650B9BB5869F064EA74AB

# https://ftp.gnu.org/gnu/bash/?C=M;O=D
ENV _BASH_VERSION 4.4
ENV _BASH_PATCH_LEVEL 0
# https://ftp.gnu.org/gnu/bash/bash-4.4-patches/?C=M;O=D
ENV _BASH_LATEST_PATCH 12
# prefixed with "_" since "$BASH..." have meaning in Bash parlance

RUN set -ex; \
  \
  apk add --no-cache --virtual .build-deps \
    bison \
    ca-certificates \
    coreutils \
    dpkg-dev dpkg \
    gcc \
    gnupg \
    libc-dev \
    make \
    ncurses-dev \
    openssl \
    patch \
    tar \
  ; \
  \
  version="$_BASH_VERSION"; \
  if [ "$_BASH_PATCH_LEVEL" -gt 0 ]; then \
    version="$version.$_BASH_PATCH_LEVEL"; \
  fi; \
  wget -O bash.tar.gz "https://ftp.gnu.org/gnu/bash/bash-$version.tar.gz"; \
  wget -O bash.tar.gz.sig "https://ftp.gnu.org/gnu/bash/bash-$version.tar.gz.sig"; \
  \
  if [ "$_BASH_LATEST_PATCH" -gt "$_BASH_PATCH_LEVEL" ]; then \
    mkdir -p bash-patches; \
    first="$(printf '%03d' "$(( _BASH_PATCH_LEVEL + 1 ))")"; \
    last="$(printf '%03d' "$_BASH_LATEST_PATCH")"; \
    for patch in $(seq -w "$first" "$last"); do \
      url="https://ftp.gnu.org/gnu/bash/bash-$_BASH_VERSION-patches/bash${_BASH_VERSION//./}-$patch"; \
      wget -O "bash-patches/$patch" "$url"; \
      wget -O "bash-patches/$patch.sig" "$url.sig"; \
    done; \
  fi; \
  \
  export GNUPGHOME="$(mktemp -d)"; \
  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$_BASH_GPG_KEY"; \
  gpg --batch --verify bash.tar.gz.sig bash.tar.gz; \
  rm bash.tar.gz.sig; \
  if [ -d bash-patches ]; then \
    for sig in bash-patches/*.sig; do \
      p="${sig%.sig}"; \
      gpg --batch --verify "$sig" "$p"; \
      rm "$sig"; \
    done; \
  fi; \
  rm -rf "$GNUPGHOME"; \
  \
  mkdir -p /usr/src/bash; \
  tar \
    --extract \
    --file=bash.tar.gz \
    --strip-components=1 \
    --directory=/usr/src/bash \
  ; \
  rm bash.tar.gz; \
  \
  if [ -d bash-patches ]; then \
    for p in bash-patches/*; do \
      patch \
        --directory=/usr/src/bash \
        --input="$(readlink -f "$p")" \
        --strip=0 \
      ; \
      rm "$p"; \
    done; \
    rmdir bash-patches; \
  fi; \
  \
  cd /usr/src/bash; \
  gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"; \
# update "config.guess" and "config.sub" to get more aggressively inclusive architecture support
  for f in config.guess config.sub; do \
    wget -O "support/$f" "https://git.savannah.gnu.org/cgit/config.git/plain/$f?id=7d3d27baf8107b630586c962c057e22149653deb"; \
  done; \
  ./configure \
    --build="$gnuArch" \
    --enable-readline \
    --with-curses \
# musl does not implement brk/sbrk (they simply return -ENOMEM)
#   bash: xmalloc: locale.c:81: cannot allocate 18 bytes (0 bytes allocated)
    --without-bash-malloc \
  || { \
    cat >&2 config.log; \
    false; \
  }; \
  make -j "$(nproc)"; \
  make install; \
  cd /; \
  rm -r /usr/src/bash; \
  \
# delete a few installed bits for smaller image size
  rm -r \
    /usr/local/share/doc/bash/*.html \
    /usr/local/share/info \
    /usr/local/share/locale \
    /usr/local/share/man \
  ; \
  \
  runDeps="$( \
    scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
      | tr ',' '\n' \
      | sort -u \
      | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
  )"; \
  apk add --no-cache --virtual .bash-rundeps $runDeps; \
  apk del .build-deps; \
  \
  [ "$(which bash)" = '/usr/local/bin/bash' ]; \
  bash --version; \
[ "$(bash -c 'echo "${BASH_VERSION%%[^0-9.]*}"')" = "$_BASH_VERSION.$_BASH_LATEST_PATCH" ];

RUN ln -s /usr/local/bin/bash /bin/bash

ENV GLIBC 2.23-r3

RUN apk update && apk add --no-cache openssl ca-certificates && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \
    apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \
    ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib

RUN apk add --no-cache --virtual curl && \
    curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

CMD ["bash"]
