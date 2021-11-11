FROM centos:7
LABEL maintainer="Nimbix, Inc."

WORKDIR /tmp

# Update SERIAL_NUMBER to force rebuild of all layers (don't use cached layers)
ARG SERIAL_NUMBER
ENV SERIAL_NUMBER ${SERIAL_NUMBER:-20210820.1100}

ARG GIT_BRANCH
ENV GIT_BRANCH ${GIT_BRANCH:-master}

# Install image-common for X, VNC and common utilities
RUN curl -H 'Cache-Control: no-cache' \
        https://raw.githubusercontent.com/nimbix/image-common/$GIT_BRANCH/install-nimbix.sh \
        | bash -s -- --setup-nimbix-desktop

COPY NAE/screenshot.png /etc/NAE/screenshot.png
COPY NAE/AppDef.json /etc/NAE/AppDef.json
RUN curl --fail -X POST -d @/etc/NAE/AppDef.json https://cloud.nimbix.net/api/jarvice/validate

# Expose port 22 for local JARVICE emulation in docker
EXPOSE 22

# for standalone use
EXPOSE 5901
EXPOSE 443
