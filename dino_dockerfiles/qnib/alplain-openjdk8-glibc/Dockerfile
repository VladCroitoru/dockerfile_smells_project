FROM qnib/alplain-openjdk8

ARG GLIBC_VER=2.23-r2

RUN apk --no-cache add curl ca-certificates bash \
 && curl -sLo /tmp/glibc.apk "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VER}/glibc-${GLIBC_VER}.apk" \
 && apk --no-cache --allow-untrusted add /tmp/glibc.apk \
 && curl -sLo /tmp/glibc-bin.apk "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VER}/glibc-bin-${GLIBC_VER}.apk" \
 && apk --no-cache --allow-untrusted add /tmp/glibc-bin.apk \
 && ldconfig /lib /usr/glibc/usr/lib
