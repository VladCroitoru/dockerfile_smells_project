FROM ubuntu

# Set up basic packages
RUN apt-get update
RUN apt-get install -y wget git make cowsay gcc
RUN ln -s /usr/games/cowsay /usr/local/bin/cowsay

# Configure the environment
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/profile.d/go.sh
RUN echo 'export GOPATH=$HOME/go' >> /etc/profile.d/go.sh

# Set up ssh client
RUN mkdir -p /root/.ssh
RUN ssh-keyscan -H bitbucket.org >> /root/.ssh/known_hosts
RUN ssh-keyscan -H github.com >> /root/.ssh/known_hosts

# Copy the buildscript
COPY build.sh /usr/local/bin/build

# Download and unpack golang archive
RUN wget https://storage.googleapis.com/golang/go1.4.linux-amd64.tar.gz -O /tmp/golang.tar.gz
RUN tar -C /usr/local -xzf /tmp/golang.tar.gz

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
