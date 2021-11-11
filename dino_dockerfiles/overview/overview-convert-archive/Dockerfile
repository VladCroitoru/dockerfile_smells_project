FROM overview/overview-convert-framework:0.0.15 as framework


FROM alpine:3.7 AS os
RUN apk add --update --no-cache jq ca-certificates


FROM alpine:3.7 AS test-base
RUN apk add --update --no-cache jq python3
WORKDIR /app


FROM alpine:3.7 AS build
ENV LIBARCHIVE_VERSION 3.3.2
RUN apk add --update --no-cache \
      build-base \
      curl \
      zlib-dev \
      bzip2-dev \
      xz-dev \
      lz4-dev \
      acl-dev \
      libressl-dev \
      expat-dev \
  && mkdir -p /build/ \
  && cd /build \
  && curl -o - http://www.libarchive.org/downloads/libarchive-${LIBARCHIVE_VERSION}.tar.gz | tar zxf - \
  && cd libarchive-${LIBARCHIVE_VERSION} \
  && ./configure --without-xml2 \
  && make -j3
WORKDIR /build/overview-convert-archive
COPY Makefile Makefile
COPY src/ src/
RUN make


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/overview-convert-archive/archive-to-multipart /app/
COPY do-convert-stream-to-mime-multipart /app/
CMD [ "/app/run" ]


FROM base AS dev


# The "test" image is special: we integration-test on Docker Hub by actually
# _running_ the tests as part of the build.
FROM test-base AS test
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/overview-convert-archive/archive-to-multipart /app/
COPY do-convert-stream-to-mime-multipart /app/
COPY /test/ /app/test/
RUN ./test/all-tests.py
CMD [ "true" ]


FROM base AS production
