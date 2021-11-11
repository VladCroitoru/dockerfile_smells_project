FROM frolvlad/alpine-glibc
MAINTAINER Félix Saparelli <me@passcod.name>
CMD ["postier"]
VOLUME /hooks

RUN apk add --update openssl curl xz &&\
    rm -rf /var/cache/apk/* &&\
    curl -L https://github.com/passcod/postier/releases/download/v1.0.1/postier-1.0.1-linux-amd64.xz > postier.xz &&\
    xz -d postier.xz &&\
    mv postier /bin/ &&\
    apk --purge del curl xz &&\
    chmod +x /bin/postier
