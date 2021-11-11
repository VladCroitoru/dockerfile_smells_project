FROM puzzle/ose3-rails:pure-241

ENV RAILS_ENV production
ENV SECRET_KEY_BASE aienhat423490g8iretuk
ENV OPENPROJECT_VERSION v7.2.3

USER root
WORKDIR /opt/app-root/src

COPY bin/ /opt/app-root/bin/
COPY .s2i/ /tmp/src/.s2i/
COPY config/ /tmp/src/config/
COPY crontab /opt/app-root/etc/
COPY Gemfile.plugins /tmp/src/
COPY apache-repos.conf /etc/httpd/conf.d/

RUN yum install -y epel-release \
 && yum -y update \
 && yum -y install python python-devel python-pip mod_perl mod_dav_svn git subversion perl-Digest-SHA perl-libwww-perl \
 && /bin/bash -c "npm install -g npm@4.0" \
 && pip install devcron \
 && git config --global user.name Openshift \
 && git config --global user.email systems@puzzle.ch \
 && mkdir /etc/httpd/Apache \
 && chown -R 1001:1001 /tmp/src \
 && chown -R 1001:1001 /opt/app-root \
 && chown -R 1001:1001 /etc/httpd/Apache \
 && chmod -R o+x /opt/app-root/bin

USER 1001
