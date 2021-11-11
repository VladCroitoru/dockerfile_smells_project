FROM ubuntu:trusty

MAINTAINER Penn Su "pennsu@gmail.com"

# Prepping install
RUN apt-get update && apt-get install -y \
  build-essential \
  m4 \
  git \
  curl \
  wget \
  bison \
  texinfo \
  zlib1g-dev \
  libssl-dev \
  libbz2-dev \
  libyaml-dev \
  libxml2-dev \
  libxslt-dev \
  libexpat-dev \
  libncurses-dev \
  libreadline-dev \
  libcurl4-openssl-dev \
  vim-nox \
  imagemagick \
  libmagickwand-dev \
  openjdk-7-jdk \
  ant \
  nodejs \
  npm \
  unzip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add users
RUN adduser web --home /home/web \
  --shell /bin/bash \
  --disabled-password \
  --gecos ""
RUN adduser cordova --home /home/cordova \
  --shell /bin/bash \
  --disabled-password \
  --gecos ""
RUN adduser linuxbrew --home /home/linuxbrew \
  --shell /bin/bash \
  --disabled-password \
  --gecos ""

# Add users to sudoers, so no need to ask for password
RUN echo "cordova ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "web ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "linuxbrew ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install rbenv to install ruby
RUN git clone git://github.com/sstephenson/rbenv.git /usr/local/rbenv
RUN echo '# rbenv setup' > /etc/profile.d/rbenv.sh
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh
RUN chmod +x /etc/profile.d/rbenv.sh

# Install rbenv plugin: ruby-build
RUN mkdir /usr/local/rbenv/plugins
RUN git clone https://github.com/sstephenson/ruby-build.git /usr/local/rbenv/plugins/ruby-build

# Let's not copy gem package documentation
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc

ENV RBENV_ROOT /usr/local/rbenv
ENV PATH /home/linuxbrew/.linuxbrew/bin:$RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Install ruby
RUN rbenv install 2.1.3
RUN rbenv global 2.1.3

RUN gem install bundler
RUN rbenv rehash

# Configure nodejs to node since the package conflict on ubuntu
RUN update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100

# Install ionic, cordova, bower, and gulp
RUN npm install -g ionic@1.2.8 cordova@3.5.0-0.2.4 bower gulp

USER linuxbrew

# Linuxbrew
RUN ruby -e "$(wget -O- https://raw.github.com/Homebrew/linuxbrew/go/install)"

RUN echo 'export PATH=~/.linuxbrew/bin:$PATH' >> ~/.bashrc
RUN echo 'export MANPATH=~/.linuxbrew/share/man:$MANPATH' >> ~/.bashrc
RUN echo 'export INFOPATH=~/.linuxbrew/share/info:$INFOPATH' >> ~/.bashrc

RUN brew update && brew install \
  python \
  awscli \
  android-sdk

# Configure android sdk
RUN echo 'export ANDROID_HOME=/home/web/.linuxbrew/opt/android-sdk' >> ~/.bashrc
RUN echo 'y' | android update sdk --no-ui -a --filter build-tools-19.0.0,platform-tools,tools,android-19,extra-android-support

CMD ["/bin/bash"]
