# v1.0
# September 2016

FROM ubuntu:xenial
MAINTAINER Fabio Rodrigues "fabio_rodrigues@student-partners.com"


#ENV http_proxy <YOUR_PROXY>
#ENV https_proxy <YOUR_PROXY>
#ENV no_proxy '127.0.0.1, 192.168.*'

ENV RUBY_VERSION 2.3.1
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

ARG user_root=root
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

# --handlerCountStartup    = set the no of worker threads to spawn at startup. Default is 5
# --handlerCountMax        = set the max no of worker threads to allow. Default is 300
# --handlerCountMaxIdle    = set the max no of idle worker threads to allow. Default is 50
ENV JENKINS_OPTS="--handlerCountStartup=5 --handlerCountMax=100 --logfile=/var/log/jenkins/jenkins.log"


# Add custom bashrc
#RUN rm /var/jenkins_home/.bashrc
#ADD ./utils/bashrc_rvm /var/jenkins_home/.bashrc

USER root

# change default bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install essentials packages
RUN apt-get update && apt-get install -y --no-install-recommends \

  build-essential \
  curl \
  gnupg \
  git \
  vim \
  subversion \
  xvfb \
  ca-certificates \
  wget \
  firefox \
  gawk \
  libreadline6-dev \
  zlib1g-dev \
  libssl-dev \
  libyaml-dev \
  libsqlite3-dev \
  autoconf \
  libgmp-dev \
  libgdbm-dev \
  libncurses5-dev \
  automake \
  libtool \
  bison \
  pkg-config \
  libffi-dev \
  sqlite3 \
  software-properties-common \
  zip


#install java
RUN add-apt-repository ppa:webupd8team/java && apt-get update

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
     echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
     DEBIAN_FRONTEND=noninteractive  apt-get install -y oracle-java8-installer oracle-java8-set-default

#updated java Home
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
# Install mysql client (no server)
RUN apt-get install -yq mysql-client libmysqlclient-dev


# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
VOLUME /var/jenkins_home
RUN curl curl -#LO https://pkg.jenkins.io/debian/jenkins-ci.org.key | apt-key add - && \
    echo 'deb http://pkg.jenkins.io/debian-stable binary/' > /etc/apt/sources.list.d/jenkins.list && \
    apt-get update && \
    apt-get install -y jenkins



USER root

# Download RVM as root
RUN curl -#LO https://rvm.io/mpapis.asc && gpg --import mpapis.asc
RUN \curl -sSL https://get.rvm.io | bash -s stable
# Install RVM requirements
RUN /bin/bash -lc "rvm requirements"
# Add jenkins to rvm group
RUN usermod -a -G rvm jenkins
ENV PATH $PATH:/usr/local/rvm/bin

USER jenkins
# Install Ruby
RUN /bin/bash -lc  "rvm install $RUBY_VERSION && rvm use $RUBY_VERSION --default"
# Set no doc for gem
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc
# Install bundler
RUN /bin/bash -lc  "gem install bundler --no-doc --no-ri"

USER root
RUN chown -R jenkins /var/jenkins_home


# slim down image
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*
# expose normal web port and slave port for jenkins
EXPOSE 8000 50000

