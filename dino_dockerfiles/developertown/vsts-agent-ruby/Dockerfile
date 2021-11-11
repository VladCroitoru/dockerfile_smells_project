FROM developertown/vsts-agent:2.107.0-1

WORKDIR /usr/local/vsts-agent

ENV AGENT_FLAVOR=Ruby \
    RUBY_VERSION=2.3.1 \
    RBENV_HOME=/usr/local/vsts-agent/.rbenv \
    RBENV_SHIMS=${RBENV_HOME}/shims \
    RUBY_HOME=${RBENV_HOME}/versions/${RUBY_VERSION} \
    CONFIGURE_OPTS=--disable-install-doc \
    rbenv=${RBENV_HOME}/bin/rbenv \
    ruby=${RBENV_SHIMS}/ruby \
    gem=${RBENV_SHIMS}/gem \
    bundle=${RBENV_SHIMS}/bundle \
    PATH=/usr/local/vsts-agent/.rbenv/shims:/usr/local/vsts-agent/.rbenv/bin:$PATH

# Install rbenv
RUN \
  #  Install rbenv \
     git clone https://github.com/rbenv/rbenv.git ~/.rbenv \
  && echo 'eval "$(rbenv init -)"' >> ~/.bashrc \
  #  Install ruby-build \
  && git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build \
  #  Install Ruby, Bundler, and Rubocop 
  && rbenv install ${RUBY_VERSION} \
  && rbenv global ${RUBY_VERSION} \
  && gem install bundler rubocop
