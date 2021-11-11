FROM alpine AS base
FROM base AS build

RUN apk add --no-cache \
      autoconf \
      automake \
      build-base \
      ca-certificates \
      curl \
      file \
      gawk \
      git \
      libtool \
      zlib-dev

RUN git clone --depth=1 --single-branch --branch=v3.5.1.1 https://github.com/google/protobuf.git

WORKDIR /protobuf

RUN ./autogen.sh \
 && CXXFLAGS="-Os" ./configure --enable-shared=false --disable-dependency-tracking --prefix=/protoc \
 && make install

RUN strip /protoc/bin/protoc

FROM base

RUN apk add --no-cache libstdc++ tini

COPY --from=build /protoc/bin/protoc /usr/bin/protoc

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/protoc"]
