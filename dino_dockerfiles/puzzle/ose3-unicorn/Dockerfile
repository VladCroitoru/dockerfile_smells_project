FROM centos/ruby-23-centos7

USER root
WORKDIR /opt/app-root/src
RUN yum install -y epel-release && \
    yum -y update && \
    yum install -y nginx mysql-devel && \
    scl enable rh-ruby23 "gem install foreman" && \
    mkdir -p /opt/app-root/etc/nginx && \
    mkdir -p /opt/app-root/bin

# Install the latest postgresql lib for pg gem
# RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
#     apt-get update && \
#     DEBIAN_FRONTEND=noninteractive \
#     apt-get install -y --force-yes libpq-dev

COPY nginx.conf /opt/app-root/etc/nginx.conf
COPY unicorn.rb /opt/app-root/etc/unicorn.rb
COPY Procfile /opt/app-root/etc/Procfile

USER 1001
ENV RAILS_ENV development
CMD foreman start -f /opt/app-root/etc/Procfile -d /opt/app-root/src
