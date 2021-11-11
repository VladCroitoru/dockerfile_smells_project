ARG VERSION=latest
FROM alpine:${VERSION}
# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG CODE_VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="Alpine Package Builder" \
#  org.label-schema.description="Let it be pulled from Readme.md..." \
  org.label-schema.url="https://github.org/hillct/docker-alpine-abuild" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url=$VCS_URL \
  org.label-schema.vendor="Colin Hill" \
  org.label-schema.version=$CODE_VERSION \
  org.label-schema.schema-version="1.0"
RUN if [ "$linux_version" = "edge" ] ; then echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories  ; else echo NOT using Testing repo ; fi
RUN apk --no-cache add alpine-sdk coreutils cmake \
  && adduser -G abuild -g "Alpine Package Builder" -s /bin/ash -D builder \
  && echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
  && mkdir /packages \
  && chown builder:abuild /packages
COPY /abuilder /bin/
USER builder
ENTRYPOINT ["abuilder", "-r"]
WORKDIR /home/builder/package
ENV RSA_PRIVATE_KEY_NAME ssh.rsa
ENV PACKAGER_PRIVKEY /home/builder/${RSA_PRIVATE_KEY_NAME}
ENV REPODEST /packages
