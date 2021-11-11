# base docker-in-docker (alpine)
FROM docker:dind
# australia/melbourne timezone
RUN apk add tzdata --no-cache \
&&  cp /usr/share/zoneinfo/Australia/Melbourne /etc/localtime \
&&  apk del -r tzdata

RUN addgroup docker -S
# s6-overlay
ENV S6_VERSION v1.18.1.5
ENV S6_URL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz

RUN apk add --no-cache curl openssl \
&&  curl -sSL ${S6_URL} | tar -C / -xzf -

# docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
&&  chmod +x /usr/local/bin/docker-compose

# install glibc reqs (https://github.com/sgerrand/alpine-pkg-glibc)
ENV GLIBC_VERSION '2.23-r3'
RUN curl -Lo /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
&&  curl -Lo glibc.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk \
&&  curl -Lo glibc-bin.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk \
&&  apk add --no-cache glibc.apk glibc-bin.apk \
&&  rm -rf /var/cache/apk/* glibc.apk glibkc-bin.apk \
&& docker-compose version

# packages
RUN apk add --no-cache git bash vim sudo


# ssh & config
RUN apk add --no-cache openssh \
&&  ssh-keygen -A


# cleanup
RUN apk del -r curl openssl \
&&  rm -rf /tmp/* \
&&  rm -rf /var/cache/apk/*

# docker service
COPY ./include/run_dockerd /etc/services.d/dockerd/run

# custom user (-e MYUSER)
COPY include/createuser /etc/cont-init.d/
RUN chmod +x /etc/cont-init.d/createuser


COPY ./include/sudoers /etc/sudoers
COPY ./include/sshd_config /etc/ssh/sshd_config
COPY ./include/run_sshd /etc/services.d/sshd/run

EXPOSE 22
# s6-overlay init
ENTRYPOINT ["/init"]
CMD []

