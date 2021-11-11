
FROM ubuntu:15.04

#================================================
# Customize sources for apt-get
#================================================
RUN  echo "deb http://archive.ubuntu.com/ubuntu vivid main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu vivid-updates main universe\n" >> /etc/apt/sources.list

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install software-properties-common \
  && add-apt-repository -y ppa:git-core/ppa

#========================
# Miscellaneous packages
# iproute which is surprisingly not available in ubuntu:15.04 but is available in ubuntu:latest
# OpenJDK8
# rlwrap is for azure-cli
# groff is for aws-cli
# tree is convenient for troubleshooting builds
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    iproute \
    openssh-client ssh-askpass\
    ca-certificates \
    openjdk-8-jdk \
    tar zip unzip \
    wget curl \
    git \
    build-essential \
    less nano tree \
    python python-pip groff \
    rlwrap \
    bison \
    libffi-dev \
    libgdbm-dev \
    libgdbm3 \
    libncurses5-dev \
    libreadline6-dev \
    libssl-dev \
    libyaml-dev \
    zlib1g-dev \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security

# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-certificates-java.postinst configure
#========================================
# Add normal user with passwordless sudo
#========================================
RUN useradd builder --shell /bin/bash --create-home \
  && usermod -a -G sudo builder \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'builder:secret' | chpasswd


RUN git clone https://github.com/sstephenson/rbenv.git /home/builder/rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git /home/builder/rbenv/plugins/ruby-build
RUN git clone https://github.com/jf/rbenv-gemset.git /home/builder/rbenv/plugins/rbenv-gemset
RUN /home/builder/rbenv/plugins/ruby-build/install.sh
ENV PATH /home/builder/rbenv/bin:$PATH
ENV RBENV_ROOT /home/builder/rbenv

RUN echo 'export RBENV_ROOT=/home/builder/rbenv' >> /etc/profile.d/rbenv.sh
RUN echo 'export PATH=/home/builder/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh

RUN echo 'export RBENV_ROOT=/home/builder/rbenv' >> .bashrc
RUN echo 'export PATH=/home/builder/rbenv/bin:/home/builder/rbenv/shims:$PATH' >> .bashrc
RUN echo 'eval "$(rbenv init -)"' >> .bashrc
RUN export PATH=/home/builder/rbenv/bin:/home/builder/rbenv/shims/:$PATH
RUN rbenv install 2.2.3 \
 && rbenv global 2.2.3 
RUN export PATH=/home/builder/rbenv/versions/2.2.3/bin:$PATH \
&& gem install bundler \
 && rbenv rehash

ENV CONFIGURE_OPTS --disable-install-doc


#==========
# Maven
#==========
ENV MAVEN_VERSION 3.3.9

RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven





#====================================
# NODE JS
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
#====================================
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash \
    && apt-get install -y nodejs

#====================================
# BOWER, GRUNT, GULP
#====================================

RUN npm install --global grunt-cli@0.1.2 bower@1.7.9 gulp@3.9.1

#====================================
# install Rbenv,Ruby 
#====================================

# use rbenv understandable version

USER builder


