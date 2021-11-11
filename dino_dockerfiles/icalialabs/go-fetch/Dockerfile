# 1: Use ruby 2.4.1 alpine as base:
FROM ruby:2.4.1-alpine

# 2: Set the application path as the working directory
WORKDIR /usr/src/app

# 3: We'll add the app's binaries path to $PATH, and set the environment name to 'production':
ENV PATH=/usr/src/app/bin:$PATH

# ==================================================================================================
# 4:  Install runtime dependencies:

# 4.1: Install the common runtime dependencies:
RUN set -ex && apk add --no-cache ca-certificates openssl tzdata su-exec

# 4.2: Install Git version > 2.5 (a fuss in alpine!)
# NOTE: git@edge can't fetch from HTTPS without libcurl@edge (it segfaults with normal libcurl)
# Hence we'll install libcurl + curl alongside git:
RUN set -ex && \
    cat /etc/apk/repositories > /tmp/repo-backup && \
    echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories && \
    apk add --no-cache --force git@edge libcurl@edge curl@edge && \
    mv -f /tmp/repo-backup /etc/apk/repositories

# 4.3: Copy just the Gemfile & Gemfile.lock, to avoid the build cache failing whenever any other
# file changed and installing dependencies all over again - a must if your'e developing this
# Dockerfile...
ADD ./Gemfile* /usr/src/app/

# 4.6: Install build dependencies AND install/build the app gems:
RUN set -ex && \
    cat /etc/apk/repositories > /tmp/repo-backup && \
    echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories && \
    apk add --no-cache --force --virtual .app-builddeps build-base@v3.4 && \
    bundle install --without development test && \
    apk del --force .app-builddeps && \
    mv -f /tmp/repo-backup /etc/apk/repositories

# ==================================================================================================
# 5: Copy the rest of the application code, then check that the app can run:
ADD . /usr/src/app
RUN set -ex && go_fetch version

# 6: Set the entrypoint
ENTRYPOINT [ "bin/go_fetch" ]

# 8: Set the default command:
CMD [ "help" ]
