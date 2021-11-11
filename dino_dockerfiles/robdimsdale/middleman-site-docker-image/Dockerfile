FROM ubuntu:trusty
MAINTAINER https://github.com/robdimsdale/

RUN \
      apt-get update && \
      apt-get -y install --fix-missing \
            build-essential \
            curl \
            git \
            libreadline6 \
            libreadline6-dev\
            wget \
      && \
      apt-get clean

# Install ruby-install
RUN curl https://codeload.github.com/postmodern/ruby-install/tar.gz/v0.5.0 | tar xvz -C /tmp/ && \
          cd /tmp/ruby-install-0.5.0 && \
          make install

# Install Ruby
RUN ruby-install ruby 2.2.2 -- --disable-install-rdoc

# Add ruby to PATH
ENV PATH $PATH:/home/root/.gem/ruby/2.2.2/bin:/opt/rubies/ruby-2.2.2/lib/ruby/gems/2.2.2/bin:/opt/rubies/ruby-2.2.2/bin

# Install gems
RUN /opt/rubies/ruby-2.2.2/bin/gem install bundler --no-rdoc --no-ri

# Set permissions on ruby directory
RUN chmod -R 777 /opt/rubies/

# Install CF CLI
RUN curl https://s3.amazonaws.com/go-cli/releases/v6.20.0/cf-cli_6.20.0_linux_x86-64.tgz | tar xvz -C /bin
