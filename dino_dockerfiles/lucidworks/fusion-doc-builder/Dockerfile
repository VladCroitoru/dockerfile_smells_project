# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node,
# plus dependencies for our build and some tools we use for testing.
# Note the plaintext password here; depending on your environment that may not be advisable.
# Based on evarga/jenkins-slave
FROM ruby:2.4

MAINTAINER  Martijn Koster "martijn.koster@lucidworks.com"

ENV PHANTOMJS_VERSION=1.9.8

RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \
  echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
  apt-get update && \
  apt-get -y install ant git openssh-server \
  build-essential libxml2-dev libxslt1-dev python-dev python-pip \
  libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
  curl netcat-openbsd net-tools procps lsof && \
  sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd && \
  mkdir -p /var/run/sshd && \
  adduser --quiet --gecos "" --disabled-password jenkins && \
  (echo "jenkins:jenkins" | chpasswd)  && \
  pip install virtualenv && \
  pip install awscli && \
  apt-get -y install vim
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \
  apt-get -y install locales && \
  sed -i.bak -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen && \
  update-locale LC_ALL="en_US.UTF-8" && \
  export LANGUAGE=en_US:en && \
  export LANG=en_US.UTF-8 && \
  export LC_ALL=en_US.UTF-8 && \
  dpkg-reconfigure locales
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \
  apt-get install libyaml-dev && \
  pip install pyyaml bs4 linkchecker && \
  apt-get -y install ruby ruby-dev nodejs && \
  gem install asciidoctor:1.5.6.1 jekyll:3.7.2 jekyll-asciidoc:2.0.1 && \
  gem install asciidoctor-pdf --version 1.5.3 && \
  gem install jekyll-toc:0.3.0.pre1 && \
  gem install coderay pygments.rb
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \
  curl -sSL https://github.com/jgm/pandoc/releases/download/1.17.2/pandoc-1.17.2-1-amd64.deb -o/tmp/pandoc.deb && \
  dpkg -i /tmp/pandoc.deb && \
  rm -f /tmp/pandoc.deb
  
RUN curl -L https://nodejs.org/dist/v8.8.0/node-v8.8.0-linux-x64.tar.xz -o /tmp/node.tar.xz && \
  tar -C /usr/local --extract --strip-components 1 --file /tmp/node.tar.xz && \
  rm /tmp/node.tar.xz

RUN npm install -g gulp && npm link gulp && gulp --version

ENV LANGUAGE en_US:en
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

EXPOSE 22 8764 4000

CMD ["/usr/sbin/sshd", "-D"]
