FROM debian:8.6
MAINTAINER Ben Hainline <benhainline@gmail.com>

# reduce footprint of package installs
COPY minify /

# install curl/deps
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

# install and verify clamav/freshclam from source
ENV CLAMAV_VERSION="0.99.2"
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y \
      build-essential \
      libpcre3-dev \
      libssl-dev && \
    curl --fail --show-error --location --output clamav-${CLAMAV_VERSION}.tar.gz -- "http://www.clamav.net/downloads/production/clamav-${CLAMAV_VERSION}.tar.gz" && \
    curl --fail --show-error --location --output clamav-${CLAMAV_VERSION}.tar.gz.sig -- "http://www.clamav.net/downloads/production/clamav-${CLAMAV_VERSION}.tar.gz.sig" && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg --keyserver pgp.mit.edu --recv-keys B3D5342C260429A0 && \
    gpg --batch --verify clamav-${CLAMAV_VERSION}.tar.gz.sig clamav-${CLAMAV_VERSION}.tar.gz && \
    tar --extract --gzip --file=clamav-${CLAMAV_VERSION}.tar.gz && \
    cd clamav-${CLAMAV_VERSION} && \
    ./configure && \
    make && make install && \
    ldconfig && \
    cd .. && rm -rf clamav-${CLAMAV_VERSION}* "${GNUPGHOME}" && \
    apt-get purge -y --auto-remove \
      build-essential \
      libpcre3-dev \
      libssl-dev && \
    rm -rf /var/lib/apt/lists*

# configure freshclam
ENV CLAM_USER="clamav" \
    CLAM_UID="1000" \
    CLAM_ETC="/usr/local/etc" \
    CLAM_DB="/usr/local/share/clamav" \
    CLAM_CHECKS="24" \
    CLAM_DAEMON_FOREGROUND="yes"
RUN useradd -u ${CLAM_UID} ${CLAM_USER} && \
    cp ${CLAM_ETC}/freshclam.conf.sample ${CLAM_ETC}/freshclam.conf && \
    sed -i "s/^Example/# Example/; \
      s/#LogTime yes/LogTime yes/; \
      s/#ScriptedUpdates yes/ScriptedUpdates no/; \
      s/#Checks 24/Checks ${CLAM_CHECKS}/; \
      s/#Foreground yes/Foreground ${CLAM_DAEMON_FOREGROUND}/" ${CLAM_ETC}/freshclam.conf && \
    mkdir ${CLAM_DB} && \
    chown ${CLAM_USER}: ${CLAM_DB} && \
    freshclam --version

# volume for virus definitions
VOLUME ["/usr/local/share/clamav"]

# entrypoint and cmd
ENTRYPOINT ["/usr/local/bin/freshclam"]
CMD ["-v"]
