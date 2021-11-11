ARG builder_base
FROM ${builder_base}

RUN \
  . /etc/os-release && [ "$VERSION_ID" != 16.04 ] && exit 0; \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    software-properties-common \
  && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
  && apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    gcc-7 g++-7 \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 10 --slave /usr/bin/g++ g++ /usr/bin/g++-5 \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 20 --slave /usr/bin/g++ g++ /usr/bin/g++-7 \
  && rm -rf /var/lib/apt/lists/*

USER builder
COPY firefox.conf /home/builder/

USER root
COPY buildenv.d/* /etc/buildenv.d/

ARG subdir
COPY ${subdir}/ /tmp/tmpdir
RUN \
  if [ -d /tmp/tmpdir/buildenv.d ]; then \
    mv /tmp/tmpdir/buildenv.d/* /etc/buildenv.d/; \
  fi; \
  if ls /tmp/tmpdir/*.conf >/dev/null 2>&1; then \
    chown builder:builder /tmp/tmpdir/*.conf; \
    mv /tmp/tmpdir/*.conf /home/builder; \
  fi

ARG firefox_version
ENV FIREFOX_VERSION=${firefox_version}
