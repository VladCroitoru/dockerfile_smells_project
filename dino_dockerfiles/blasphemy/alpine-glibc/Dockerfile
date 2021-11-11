FROM alpine
ARG GLIBC_VERSION=2.23-r3
RUN apk --no-cache add ca-certificates wget \
 && wget -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
 && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \
 && apk add glibc-2.23-r3.apk --no-cache \
 && rm glibc-2.23-r3.apk \
 && rm /etc/apk/keys/sgerrand.rsa.pub \
 && apk del wget ca-certificates --no-cache
