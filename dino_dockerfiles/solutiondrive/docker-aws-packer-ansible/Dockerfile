ARG PACKER_VERSION

FROM hashicorp/packer:${PACKER_VERSION}

ARG ANSIBLE_VERSION
ARG AWSCLI_VERSION
ARG INSPEC_VERSION
ENV PATH /usr/local/rbenv/shims:/usr/local/rbenv/bin:$PATH
ENV RBENV_ROOT /usr/local/rbenv
ENV RUBY_VERSION 2.6.6
ENV CONFIGURE_OPTS --disable-install-doc

RUN apk update && \
    apk upgrade && \
    apk --no-cache add python3 py3-pip ca-certificates openssh-client ruby ruby-rdoc ruby-irb bash && \
    apk --no-cache add --virtual .sd-build-dependencies gcc libffi-dev openssl-dev git musl-dev curl shadow tar \
        build-base ruby-dev python3-dev linux-headers gnupg procps yaml yaml-dev libtool make readline readline-dev zlib zlib-dev openssl \
        alpine-sdk imagemagick-dev wget vim xvfb autoconf bison bzip2 bzip2-dev coreutils gdbm-dev libc-dev \
        libxml2-dev libxslt-dev ncurses-dev

RUN apk --no-cache add --virtual .sd-build-dependencies-failable libssl1.0 qt-webkit ;\
    exit 0

RUN git clone --depth 1 git://github.com/sstephenson/rbenv.git ${RBENV_ROOT} \
        &&  git clone --depth 1 https://github.com/sstephenson/ruby-build.git ${RBENV_ROOT}/plugins/ruby-build \
        &&  git clone --depth 1 git://github.com/jf/rbenv-gemset.git ${RBENV_ROOT}/plugins/rbenv-gemset \
        && ${RBENV_ROOT}/plugins/ruby-build/install.sh

RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh \
&&  echo 'eval "$(rbenv init -)"' >> /root/.bashrc

RUN rbenv install $RUBY_VERSION \
&&  rbenv global $RUBY_VERSION

RUN gem install bundler

# Configure python3
RUN pip3 install --upgrade pip setuptools && \
    ln -s /usr/bin/python3 /usr/bin/python

RUN pip install awscli==${AWSCLI_VERSION} ansible==${ANSIBLE_VERSION}
RUN gem install inspec -v ${INSPEC_VERSION} \
    && gem install ed25519 rbnacl rbnacl-libsodium bcrypt_pbkdf

# Cleanup
RUN apk --no-cache del .sd-build-dependencies-failable; exit 0
RUN apk --no-cache del .sd-build-dependencies \
    && rm -rf /tmp/*

ADD keyscan.sh /bin/keyscan.sh
RUN chmod +x /bin/keyscan.sh && \
    sync && \
    /bin/keyscan.sh github.com nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8 && \
    /bin/keyscan.sh bitbucket.org zzXQOXSRBEiUtuE8AikJYKwbHaxvSc0ojez9YXaGp1A

ADD run.sh /bin/run.sh

ENTRYPOINT ["/bin/bash", "/bin/run.sh"]
