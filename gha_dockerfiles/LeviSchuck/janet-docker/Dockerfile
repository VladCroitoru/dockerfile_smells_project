FROM alpine:3.14 as alpine-base
ENV PATH="/app/bin:$PATH"

FROM alpine-base as alpine-dev
RUN apk add --no-cache gcc musl-dev make git build-base man-pages

FROM alpine-dev as build
WORKDIR /build
ARG COMMIT=HEAD
RUN git clone https://github.com/janet-lang/janet.git . && \
  git checkout $COMMIT && \
  make PREFIX=/app -j && \
  make test && \
  make PREFIX=/app install
WORKDIR /jpm
RUN git clone --depth=1 https://github.com/janet-lang/jpm.git . && \
  PREFIX=/app /app/bin/janet bootstrap.janet

FROM alpine-dev as dev
COPY --from=build /app /app/

WORKDIR /
CMD ["ash"]

FROM alpine-base as core
COPY --from=build /app/ /app/
WORKDIR /
CMD ["janet"]
