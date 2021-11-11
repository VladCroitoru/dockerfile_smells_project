# Copyright (c) 2021 Jesse N. <jesse@keplerdev.com>
# This work is licensed under the terms of the MIT license. For a copy, see <https://opensource.org/licenses/MIT>.

ARG VARIANT=3.14 \
    TZ=America/New_York

FROM alpine:"$VARIANT" as root

LABEL maintainer="Jesse N. <jesse@keplerdev.com>" \
    org.opencontainers.image.source=https://github.com/jessenich/docker-alpine/blob/main/Dockerfile

ENV VARIANT="$VARIANT" \
    HOME="/home/$NON_ROOT_ADMIN" \
    TZ="$TZ" \
    RUNNING_IN_DOCKER=true

USER root

COPY ./rootfs /
RUN chmod ug+wrx /usr/sbin/addsudouser.sh && \
    chmod ug+wrx /usr/sbin/entrypoint.sh
RUN apk --update --no-cache add \
        ca-certificates \
        nano \
        nano-syntax \
        rsync \
        curl \
        wget \
        tzdata \
        jq \
        yq;

FROM root as sudo
ENV USER="sysadm"

RUN apk --update --no-cache add shadow sudo

ENTRYPOINT [ "/usr/sbin/entrypoint", "$USER" ]
WORKDIR "/home/$USER"
USER "$USER"
