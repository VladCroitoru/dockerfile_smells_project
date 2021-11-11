FROM alpine:3.11 AS build

ENV GLIBC_VER=2.31-r0

# install glibc compatibility for alpine
RUN apk add --no-cache --virtual .build-deps \
    binutils \
    curl
RUN curl -sL https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub
RUN curl -sLO https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VER}/glibc-${GLIBC_VER}.apk
RUN curl -sLO https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VER}/glibc-bin-${GLIBC_VER}.apk
RUN apk add --no-cache \
    glibc-${GLIBC_VER}.apk \
    glibc-bin-${GLIBC_VER}.apk

RUN apk -U add groff less python py-pip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

FROM docker:20-git
RUN apk add --no-cache \
    curl \
    openssl \
    bash \
    groff

ADD https://codecov.io/bash /bin/codecov
RUN chmod +x /bin/codecov

COPY --from=build /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /usr/lib/ /usr/lib/
COPY --from=build /lib64 /lib64
COPY --from=build /usr/glibc-compat/ /usr/glibc-compat/
COPY --from=build /lib/ld-linux-x86-64.so.2 /lib/