# Start with a base Ubuntu 14:04 image
FROM ubuntu:trusty

MAINTAINER Mark Stratmann <mark@stratmann.me.uk>

# Set up user environment
ENV DEBIAN_FRONTEND noninteractive
RUN adduser --disabled-password --gecos "" nuser && echo "nuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# set HOME so 'npm install' and 'bower install' don't write to /
ENV HOME /home/nuser
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.en
ENV LC_ALL en_US.UTF-8
USER nuser
# RUN sudo locale-gen

# Add all base dependencies
RUN sudo apt-get update # Updated 2015-06-23
RUN sudo apt-get install -y language-pack-en-base
RUN sudo apt-get install -y vim curl
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install -y git-core
RUN sudo apt-get install -y man
RUN sudo apt-get install -y dnsutils

# Install the latest AWS cli - needed for S3 command line actions in scripts
RUN sudo apt-get install -y python-pip
RUN sudo pip install awscli

# Install RVM and RUBY
RUN /bin/bash -l -c "gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3"
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"
RUN /bin/bash -l -c "rvm get stable --auto-dotfiles"
RUN /bin/bash -l -c "rvm install 2.2.3"
RUN /bin/bash -l -c "rvm alias create default 2.2.3"

# Install NVM and Node
RUN /bin/bash -l -c "curl https://raw.githubusercontent.com/creationix/nvm/v0.17.3/install.sh | bash"
RUN /bin/bash -l -c "echo 'source ~/.nvm/nvm.sh' >> ~/.profile"
ENV PATH $HOME/.nvm/bin:$PATH
RUN /bin/bash -l -c "nvm install v4.3"
RUN /bin/bash -l -c "nvm alias default 4.3"
RUN /bin/bash -l -c "npm install -g gulp"
RUN /bin/bash -l -c "npm install -g grunt-cli"

# Add the application to the container (cwd)
WORKDIR /stockflare
RUN sudo chown -R nuser:nuser /stockflare/

# Create Gemset
RUN /bin/bash -l -c "rvm gemset create stockflare"
RUN /bin/bash -l -c "rvm use 2.2.3@stockflare --default"

RUN sudo apt-get autoremove -y

# Copy across the rest of the code
ADD . /stockflare
RUN sudo chown -R nuser:nuser .

RUN /bin/bash -l -c "npm install"

WORKDIR /stockflare/worker
RUN /bin/bash -l -c "npm install"
WORKDIR /stockflare

VOLUME ["/stockflare"]


# Setup the entrypoint
ENTRYPOINT ["/bin/bash", "-l", "-c"]
