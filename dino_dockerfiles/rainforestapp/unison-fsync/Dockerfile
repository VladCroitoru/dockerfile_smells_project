FROM alpine:3.7
WORKDIR /build
RUN apk update \
    && apk add build-base ocaml \
    && wget https://github.com/bcpierce00/unison/archive/v2.51.2.tar.gz \
    && tar xzf v2.51* \
    && cd unison-* \
    && sed -i 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/' src/fsmonitor/linux/inotify_stubs.c \
    && UISTYLE=text STATIC=true make \
    && mkdir /out \
    && cp src/unison /out \
    && cp src/unison-fsmonitor /out

FROM alpine:3.7
COPY --from=0 /out/* /usr/bin/
WORKDIR /data
ENTRYPOINT unison -socket 5000
