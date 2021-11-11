FROM nginx:1.21.0-alpine
MAINTAINER Manuel Andres Garcia Vazquez "<manuel.vazquez@intraway.com>"

ARG BUILD_DATE
ARG BUILD_VCS_REF
ARG BUILD_VERSION
ARG CREATEREPO_C_VERSION

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/intraway/docker-yumrepo.git" \
      org.label-schema.vcs-ref=$BUILD_VCS_REF \
      org.label-schema.version=$BUILD_VERSION \
      com.microscaling.license=GPL-3.0

# NOTE: arguments include operator ('=' / '>' / '<' / '=~' ...)
# Default to empty to always pick latest available...
# ENV CREATEREPO_C_VERSION=${CREATEREPO_C_VERSION:->0.17.1-r0}
# ENV INOTIFY_TOOLS_VERSION=${INOTIFY_TOOLS_VERSION:->3.20.11.0-r0}
# ENV GNUPG_VERSION=${GNUPG_VERSION:->2.2.31-r0}

ENV REPO_PORT=${REPO_PORT:-80}
ENV REPO_PROTO=${REPO_PROTO:-http}
ENV REPO_PATH=${REPO_PATH:-/var/repo}
ENV REPO_DEPTH=${REPO_DEPTH:-2}

EXPOSE ${REPO_PORT}

WORKDIR /tmp

########## Install CreateRepo ##########
RUN echo -e "http://dl-cdn.alpinelinux.org/alpine/edge/main\n\
http://dl-cdn.alpinelinux.org/alpine/edge/community\n\
http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories &&\
    apk add --no-cache \
        createrepo_c${CREATEREPO_C_VERSION} \
        inotify-tools${INOTIFY_TOOLS_VERSION} \
        gnupg${GNUPG_VERSION}
########################################

############# Config NginX #############
ADD extras/yumrepo.sh /bin/yumrepo.sh
RUN rm -f /etc/nginx/conf.d/* &&\
    mkdir -p ${REPO_PATH} &&\
    chown -R nginx.nginx ${REPO_PATH} &&\
    sed -i '/user  nginx;/a daemon off;' /etc/nginx/nginx.conf &&\
    chmod a+x /bin/yumrepo.sh
ADD extras/nginx/repo.conf /etc/nginx/conf.d/repo.conf
########################################

ENTRYPOINT ["/bin/sh"]
CMD ["/bin/yumrepo.sh"]
