FROM xmlangel/base-ubuntu
VOLUME /home

#RUN curl -L http://www.opscode.com/chef/install.sh | sudo bash
#RUN apt-get install -y ruby-full
#기본개발툴설치
RUN apt-get install -y build-essential
RUN apt-get install -y curl openssl

#ruby 2.0.0 설치
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=2.0.0
#rvm 실행
#RUN source /etc/profile.d/rvm.sh
# RUN /etc/profile.d/rvm.sh

# basics
#RUN apt-get install -y vim
#RUN apt-get install -y git-core
#RUN apt-get install -y nano
#RUN apt-get install -y openssl libreadline6 libreadline6-dev curl zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion pkg-config

# #Ruby 2.0.0 설치
# install RVM, Ruby, and Bundler
#RUN \curl -L https://get.rvm.io | bash -s stable
#RUN /bin/bash -l -c "rvm requirements"
#RUN /bin/bash -l -c "rvm install 2.0"
#RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"

 
# #Ruby 2.0.0을 default로 사용
#RUN /bin/bash -l -c "rvm use 2.0.0 --default"

# Set locale to avoid apt-get warnings in OSX
RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8
ENV LC_ALL C
ENV LC_ALL en_US.UTF-8

# Install chef and its prerequisites
# NOTE: libgecode-dev required by dep-selector-libgecode in berfshelf
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      curl \
      git \
      build-essential \
      libxml2-dev \
      libxslt-dev && \
    apt-get install -y --no-install-recommends libgecode-dev && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN curl -L https://www.opscode.com/chef/install.sh | bash && \
    echo 'gem: --no-ri --no-rdoc' > ~/.gemrc

# Install berkshelf
# See https://github.com/opscode/dep-selector-libgecode/issues/15
RUN USE_SYSTEM_GECODE=1 /opt/chef/embedded/bin/gem install berkshelf

# Clean up
RUN rm -rf /tmp/* /var/tmp/*
