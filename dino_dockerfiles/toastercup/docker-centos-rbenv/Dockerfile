FROM centos:centos7
MAINTAINER Alex Tharp "toastercup@gmail.com"

# Environmental variables
ENV APP_NAME webapp
ENV APP_USER $APP_NAME
ENV APP_GROUP $APP_NAME
ENV APP_PATH /${APP_NAME}

# Update system, despite a warning against this: https://docs.docker.com/articles/dockerfile_best-practices/#run
# The official CentOS Dockerfiles repo recommends it: https://github.com/CentOS/CentOS-Dockerfiles/blob/master/nginx/centos7/Dockerfile#L10
RUN yum -y update

# Install rbenv system dependencies
RUN yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel libyaml-devel libffi-devel \
  openssl-devel make bzip2 autoconf automake libtool bison iconv-devel git-core

# Clean up yum cache
RUN yum clean all

# Create the unprivileged application user, group and directory, and switch user
RUN groupadd $APP_GROUP; useradd -g $APP_GROUP --home-dir $APP_PATH $APP_USER
USER $APP_USER
ENV HOME $APP_PATH

# Setup unprivileged user environmental variables
ENV RBENV_ROOT ${HOME}/.rbenv
ENV PATH ${RBENV_ROOT}/bin:${RBENV_ROOT}/shims:$PATH

# Install rbenv, ruby-build
RUN git clone git://github.com/sstephenson/rbenv.git $RBENV_ROOT
RUN git clone git://github.com/sstephenson/ruby-build.git ${RBENV_ROOT}/plugins/ruby-build
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

### ONBUILD ###
ONBUILD USER $APP_USER

# Install ruby specified in .ruby-version
ONBUILD COPY .ruby-version ${APP_PATH}/
ONBUILD WORKDIR $APP_PATH
ONBUILD ENV CONFIGURE_OPTS --disable-install-doc
ONBUILD RUN rbenv install; rbenv init -

# Set gem config
ONBUILD RUN mkdir $( dirname $(ruby -e 'print Gem::ConfigFile::SYSTEM_WIDE_CONFIG_FILE') )
ONBUILD RUN echo 'gem: --no-document' >> $(ruby -e 'print Gem::ConfigFile::SYSTEM_WIDE_CONFIG_FILE')

# Install bundler, rehash
ONBUILD RUN gem install bundler; rbenv rehash

# Switch back to root for the parent image
ONBUILD USER root
