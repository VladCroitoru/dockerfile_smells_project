FROM ubuntu
MAINTAINER Takashi Takebayashi <changesworlds@gmail.com>

# Install packages for building Ruby, npm, Node.js
# Update-alternative nodojs to node
# Update npm
RUN apt-get update && \
    apt-get install -y --force-yes \
     build-essential \
     curl \
     git \
     libreadline-dev \
     libssl-dev \
     libyaml-dev \
     libxml2-dev \
     nodejs \
     npm \
     zlib1g-dev && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10 && \
    npm install npm -g && \
    git clone https://github.com/sstephenson/rbenv.git /root/.rbenv && \
    git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build && \
    ./root/.rbenv/plugins/ruby-build/install.sh && \
    echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh && \
    chmod -R 755 /root/.rbenv/bin

ENV PATH="/root/.rbenv/bin:$PATH" \
    CONFIGURE_OPTS='--disable-install-doc'
COPY ./ruby-versions.txt /root/ruby-versions.txt

# Install multiple versions of ruby
# Install Bundler for each version of ruby
# Install the agent installer
# Create Agent
RUN xargs -L 1 rbenv install < /root/ruby-versions.txt && \
    echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \
    bash -l -c 'for v in $(cat /root/ruby-versions.txt); do rbenv global $v; gem install bundler; done' && \
    npm install -g vsoagent-installer && \
    mkdir /opt/myagent && \
    cd /opt/myagent && \
    vsoagent-installer && \
    echo "vsoagent\nvsoagent\n\n\n\n\n\n\n" | adduser vsoagent && \
    chown -R vsoagent /opt/myagent

WORKDIR /opt/myagent
ENTRYPOINT /bin/bash
