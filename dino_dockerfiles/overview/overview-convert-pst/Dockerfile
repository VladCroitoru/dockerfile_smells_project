FROM overview/overview-convert-framework:0.0.17 as framework


FROM alpine:3.7 AS os
RUN apk add --update --no-cache ca-certificates jq


FROM alpine:3.7 AS test-base
RUN apk add --update --no-cache bats jq
WORKDIR /app


FROM alpine:3.7 AS build
# Install programs used for building.
#
# libpst depends on C++ and libgsf (which depends on libxml2) for its .msg
# feature, which we don't use. It would be nice if ./configure made that
# optional. But let's just install all the extra stuff anyway.
RUN \
  apk add --update --no-cache \
    ca-certificates \
    curl \
    musl-dev \
    gcc \
    g++ \
    make \
    tar \
    intltool \
    gzip \
    glib-dev \
    glib-static \
    xz
# libxml2: alpine doesn't statically link it in libxml2-dev, so we'll compile
# it manually. (libgsf requires it.)
ENV LIBXML2_VERSION=2.9.8
RUN \
  mkdir -p /build \
  && cd /build \
  && curl -o - ftp://xmlsoft.org/libxml2/libxml2-${LIBXML2_VERSION}.tar.gz | tar zxf - \
  && cd libxml2-${LIBXML2_VERSION} \
  && ./configure --without-python \
  && make -j4 && make install
# libgsf: alpine doesn't statically link it in libgsf-dev, so we'll compile
# it manually.
ENV LIBGSF_VERSION=1.14.43
RUN \
  mkdir -p /build \
  && cd /build \
  && curl -o - --location http://ftp.gnome.org/pub/gnome/sources/libgsf/1.14/libgsf-${LIBGSF_VERSION}.tar.xz | tar Jxf - \
  && cd libgsf-${LIBGSF_VERSION} \
  && ./configure \
  && make -j4 && make install
# Install libpst
ENV LIBPST_VERSION=0.6.72
RUN \
  mkdir -p /build \
  && cd /build \
  && curl -o - --location http://www.five-ten-sg.com/libpst/packages/libpst-${LIBPST_VERSION}.tar.gz | tar zxf - \
  && cd libpst-${LIBPST_VERSION} \
  && ./configure --disable-python --enable-libpst-shared \
  && make -j4 && make install
# Build
WORKDIR /build/convert-emailarchive
COPY Makefile Makefile
COPY src/ src/
RUN make


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/convert-emailarchive/extract-pst /app/
COPY do-convert-stream-to-mime-multipart /app/
CMD [ "/app/run" ]


FROM base AS dev


# The "test" image is special: we integration-test on Docker Hub by actually
# _running_ the tests as part of the build.
FROM test-base AS test
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/convert-emailarchive/extract-pst /app/
COPY do-convert-stream-to-mime-multipart /app/
COPY /test/ /app/test/
RUN ./test/suite.bats
CMD [ "true" ]


FROM base AS production
