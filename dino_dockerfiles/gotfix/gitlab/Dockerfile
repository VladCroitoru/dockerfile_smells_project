FROM ubuntu:xenial
MAINTAINER ian@phpb.com

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_BRANCH
ARG VERSION

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="Docker Gitlab CE" \
      org.label-schema.description="Dockerized Gitlab CE built from source" \
      org.label-schema.usage="https://gotfix.com/docker/gitlab/blob/master/README.md" \
      org.label-schema.url="https://gotfix.com/docker/gitlab" \
      org.label-schema.vcs-url=https://gotfix.com/docker/gitlab.git \
      org.label-schema.vendor="Ian Matyssik <ian@phpb.com>" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.build-date="${BUILD_DATE}" \
      com.gotfix.maintainer="ian@phpb.com" \
      com.gotfix.license=MIT \
      com.gotfix.docker.dockerfile="/Dockerfile"

ENV GITLAB_VERSION=9.3.9 \
    RUBY_VERSION=2.3 \
    GOLANG_VERSION=1.8.3 \
    GITLAB_MONITOR_VERSION=1.9.0 \
    GITLAB_USER="git" \
    GITLAB_HOME="/home/git" \
    GITLAB_LOG_DIR="/var/log/gitlab" \
    GITLAB_CACHE_DIR="/etc/docker-gitlab" \
    RAILS_ENV=production \
    NODE_ENV=production \
    DEBIAN_FRONTEND=noninteractive

ENV GITLAB_INSTALL_DIR="${GITLAB_HOME}/gitlab" \
    GITLAB_SHELL_INSTALL_DIR="${GITLAB_HOME}/gitlab-shell" \
    GITLAB_WORKHORSE_INSTALL_DIR="${GITLAB_HOME}/gitlab-workhorse" \
    GITLAB_PAGES_INSTALL_DIR="${GITLAB_HOME}/gitlab-pages" \
    GITLAB_MONITOR_INSTALL_DIR="${GITLAB_HOME}/gitlab-monitor" \
    GITLAB_GITALY_INSTALL_DIR="${GITLAB_HOME}/gitaly" \
    GITLAB_DATA_DIR="${GITLAB_HOME}/data" \
    GITLAB_BUILD_DIR="${GITLAB_CACHE_DIR}/build" \
    GITLAB_RUNTIME_DIR="${GITLAB_CACHE_DIR}/runtime"

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    net-tools \
    sudo \
    tzdata \
    unzip \
    curl \
    vim.tiny

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E1DD270288B4E6030699E45FA1715D88E1DF1F24 \
 && echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu xenial main" >> /etc/apt/sources.list \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 80F70E11F0F0D5F10CB20E62F5DA5F09C3173AA6 \
 && echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main" >> /etc/apt/sources.list \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 136221EE520DDFAF0A905689B9316A7BC7917B12 \
 && echo "deb http://ppa.launchpad.net/chris-lea/redis-server/ubuntu xenial main" >> /etc/apt/sources.list \
 && curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
 && echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' > /etc/apt/sources.list.d/pgdg.list \
 && curl -sL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
 && echo 'deb https://deb.nodesource.com/node_7.x xenial main' > /etc/apt/sources.list.d/nodesource.list \
 && curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
 && echo 'deb https://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list \
 && apt-get update \
 && apt-get -yy upgrade \
 && apt-get -yy dist-upgrade

RUN apt-get install -y \
    gettext-base \
    git-core \
    libpq5 \
    libyaml-0-2 \
    libssl1.0.0 \
    libgdbm3 \
    libreadline6 \
    libncurses5 \
    libffi6 \
    libkrb5-3 \
    libxml2 \
    libxslt1.1 \
    libcurl3 \
    libicu55 \
    libre2-dev \
    libmysqlclient20 \
    logrotate \
    locales \
    mysql-client \
    nodejs \
    openssh-server \
    postgresql-client \
    python2.7 \
    python-docutils \
    redis-tools \
    ruby${RUBY_VERSION} \
    supervisor \
    yarn \
    zlib1g \
 && find /usr/share/locale -mindepth 1 -maxdepth 1 ! -name 'en' | xargs rm -r 

# Prepare OS for gitlab-ce
RUN update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \
 && locale-gen en_US.UTF-8 \
 && dpkg-reconfigure locales \
 && sed 's/session\s*required\s*pam_loginuid.so/session optional pam_loginuid.so/g' -i /etc/pam.d/sshd \
 && rm -rf /etc/update-motd.d /etc/motd /etc/motd.dynamic \
 && ln -fs /dev/null /run/motd.dynamic

RUN gem install bundler --no-ri --no-rdoc

COPY assets/build/ ${GITLAB_BUILD_DIR}/
COPY assets/runtime/ ${GITLAB_RUNTIME_DIR}/
RUN bash ${GITLAB_BUILD_DIR}/install.sh

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

# In order: SSH, WORKHORSE. gitlab-pages, gitlab-pages prometheus, gitaly prometheus, gitlab-monitor prometheus
EXPOSE 22/tcp 8181/tcp 8090/tcp 9235/tcp 9236/tcp 9168/tcp

VOLUME ["${GITLAB_DATA_DIR}", "${GITLAB_LOG_DIR}"]
WORKDIR ${GITLAB_INSTALL_DIR}
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["app:start"]
