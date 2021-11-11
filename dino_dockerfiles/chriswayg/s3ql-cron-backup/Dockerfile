FROM alpine:latest
LABEL maintainer="Christian Wagner https://github.com/chriswayg"
ENV TERM="xterm"

ENV S3QL_CACHE_DIR="/root/.s3ql"
ENV S3QL_AUTHINFO_FILE="/root/.s3ql/authinfo2"
ENV S3QL_MOUNT_OPTIONS="--allow-other"
ENV S3QL_MOUNTPOINT="/mnt/s3ql"
ENV S3QL_PREFIX="default"
ENV S3QL_CRONTAB="@daily echo 'No backup command has been set!'"

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.9/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=5ddf8ea26b56d4a7ff6faecdd8966610d5cb9d85

# Install dependencies.
RUN apk --no-cache add --update \
      coreutils \
      util-linux \
      tar \
      grep \
      curl \
      psmisc \
      procps \
      openssl \
      rsync \
      python3 \
      fuse \
      sqlite-libs \
      build-base \
      python3-dev \
      attr-dev \
      fuse-dev \
      sqlite-dev \
      musl-dev \
      libffi-dev \
      openssl-dev \
 # Upgrade pip and install Python module dependencies
 && pip3 install --upgrade pip \
 && pip3 install cryptography defusedxml requests apsw llfuse dugong setuptools pytest google-auth-oauthlib google-auth 
RUN cd /tmp \
 # Determine latest version of s3ql and download source code
 && S3QL_VERSION=$(wget -q https://raw.githubusercontent.com/s3ql/s3ql/master/Changes.txt -O - | grep -m1  "20" | grep -P -o '[0-9]+\.[0-9]+$') \
 && echo "*** Downloading S3QL Version: ${S3QL_VERSION}" \
 && wget -q  https://github.com/s3ql/s3ql/releases/download/release-${S3QL_VERSION}/s3ql-${S3QL_VERSION}.tar.bz2  \
 && tar jxf s3ql-${S3QL_VERSION}.tar.bz2 \
 && cd /tmp/s3ql-${S3QL_VERSION} \
 # Build s3ql and run tests \
 && python3 setup.py build_ext --inplace \
 && mkdir -pv /root/.s3ql/ \
 && python3 -m pytest -rs tests/ \
 # Install s3ql in /usr
 && python3 setup.py install 
 # Add cron for containers
RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
 && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic
 # Remove build related stuff
RUN pip3 uninstall -y pytest \
 && apk del grep curl build-base python3-dev attr-dev fuse-dev sqlite-dev musl-dev libffi-dev openssl-dev \
 && rm -r /tmp/s3ql-* \
 && echo -e "*** Installed \c" \
 && mount.s3ql --version 


# Copy docker-entrypoint, s3ql
COPY ./scripts/ /usr/local/bin/

ENTRYPOINT ["docker-entrypoint"]
