FROM malept/rust-ruby-container:base

RUN ruby-install --system --latest --cleanup ruby && \
    ruby --version && \
    gem install bundler
