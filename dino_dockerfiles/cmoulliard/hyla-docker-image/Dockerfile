# Dockerfile for a Hyla Ruby container.
#
# Provides an environment for running Hyla Ruby command line tool.
# 


#
FROM       fedora:21
MAINTAINER Charles Moulliard <ch007m@gmail.com>

# Execute system update
RUN yum -y update; yum clean all

# Install packages necessary to deploy Ruby
RUN yum -y install \
    git            \
    wget           \
    unzip          \
    tar            \
    make           \
    libtool        \
    gcc-c++        \
    gcc            \
    libssl-dev     \
    openssl-devel  \
    libyaml-devel  \
    libffi-devel   \
    readline-devel \
    zlib-devel     \
    gdbm-devel     \
    ncurses-devel  \
    pwgen          \
    sudo           \
    net-tools      \
    && yum clean all

#
# Create a user and group used to launch processes
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,
# so there is a high chance that this ID will be equal to the current user
# making it easier to use volumes (no permission issues)
#
RUN groupadd -r default -g 1000 && useradd -u 1000 -r -g default -m -d /home/default -s /sbin/nologin -c "Default user" default   

#
# Add user to sudo
#
RUN echo 'default:secret' | chpasswd
RUN echo '%default ALL=(ALL) ALL' >> /etc/sudoers 

# Set the working directory to default' user home directory
WORKDIR /home/default

USER default

#
# Include files from local folder
#
ADD . /home/default/data

#
# Install Ruby RBENV & Ruby-Build to manage the Ruby version
#
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv

RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile; \
    echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

# 
# Add Ruby, RBENV to the Path
#
ENV HOME          /home/default
ENV RBENV         $HOME/.rbenv 
ENV PATH          $RBENV/bin:$PATH
ENV RUBY_VERSION  1.9.3-p484
ENV GEM_HOME      $HOME/.gem
ENV GEM_PATH      $HOME/.gem
ENV PATH          $HOME/.gem/bin:$RBENV/versions/$RUBY_VERSION/bin:$PATH

RUN mkdir -p ~/.rbenv/plugins/;                                                          \
    git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build; \
    rbenv install 1.9.3-p484;                                                            \
    rbenv global 1.9.3-p484

# 
# Install Ruby Bundler & Pry
#
RUN gem install bundler pry --no-rdoc --no-ri

#
# Update Rubygems
#
RUN gem update --system --no-rdoc --no-ri

#
# Install Hyla gtom Gem Repo
#
RUN gem install hyla -v 1.0.7.pre.1 --no-rdoc --no-ri

# Expose PORT
EXPOSE 7000

