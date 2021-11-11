FROM alpine:3.5

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.name="alpine-mono-sdk" \
      org.label-schema.description="The Build Container pattern base: Alpine Linux 3.5, Mono built against musl, NuGet and Paket." \
      org.label-schema.url="https://github.com/makovich/alpine-mono-sdk" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/makovich/alpine-mono-sdk" \
      org.label-schema.version="$VERSION" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd.debug="docker run --rm -ti --cap-add=SYS_PTRACE /bin/sh"

RUN apk add --no-cache \
        alpine-sdk \
        linux-headers \
        python2 \
        autoconf \
        automake \
        cmake \
        libtool \
        gettext-dev \
        zlib-dev \
        strace \
        lsof \
        htop

ENV MONO_VERSION 4.8.0.495
ENV PAKET_VERSION 3.35.3
ENV NUGET_VERSION 3.5.0

COPY *.patch /mono-patch/

RUN git clone --depth 1 --single-branch --branch mono-${MONO_VERSION} https://github.com/mono/mono.git /mono-src \

 && cd /mono-src \
 && for p in /mono-patch/*.patch; do echo "Applying $p"; patch -p1 < $p; done \

 && ./autogen.sh \
        --prefix=/usr \
        --sysconfdir=/etc \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --localstatedir=/var \
        --disable-boehm \
        --with-mcs-docs=no \

 && make get-monolite-latest \
 && make \
 && make install \

 && rm -rf /mono-src \

 && mcs --version \
 && mono --version

RUN cert-sync /etc/ssl/certs/ca-certificates.crt

RUN curl -sL https://raw.githubusercontent.com/fsprojects/Paket/${PAKET_VERSION}/install.sh | /bin/sh \
 && paket --version

RUN wget -P /usr/lib/mono https://dist.nuget.org/win-x86-commandline/v${NUGET_VERSION}/nuget.exe \
 && echo -e '#!/bin/sh\nexec /usr/bin/mono $MONO_OPTIONS /usr/lib/mono/nuget.exe "$@"' > /usr/bin/nuget \
 && chmod a+x /usr/bin/nuget \
 && nuget
