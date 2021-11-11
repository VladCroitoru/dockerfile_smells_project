FROM centos:7 as builder

ENV RUBY_VERSION 2.5.5
ENV CONFIGURE_OPTS --disable-install-doc
ENV RBENV_ROOT /usr/local/rbenv
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH

# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
  && { \
    echo 'install: --no-document'; \
    echo 'update: --no-document'; \
  } >> /usr/local/etc/gemrc

# install dev tools
RUN yum install -y \
      unzip \
      tar \
      gzip \
      openssl-devel \
      readline-devel \
      zlib-devel \
      git \
      bzip2 \
      gcc \
      make

RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \
    &&  git clone git://github.com/rbenv/ruby-build.git /usr/local/rbenv/plugins/ruby-build \
    &&  git clone git://github.com/jf/rbenv-gemset.git /usr/local/rbenv/plugins/rbenv-gemset \
    &&  /usr/local/rbenv/plugins/ruby-build/install.sh

RUN eval "$(rbenv init -)"; rbenv install $RUBY_VERSION \
&&  eval "$(rbenv init -)"; rbenv global $RUBY_VERSION \
&&  eval "$(rbenv init -)"; gem update --system \
&&  eval "$(rbenv init -)"; gem install -f bundler

FROM centos:7

ENV VAGRANT_VERSION 2.2.3
ENV VIRTUALBOX_VERSION latest
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH

COPY --from=builder /usr/local/rbenv /usr/local/rbenv

RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \
&&  echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \
&&  echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh

RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \
&&  echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \
&&  echo 'eval "$(rbenv init -)"' >> /root/.bashrc

RUN cd /tmp && \
    curl -o vagrant.rpm https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm && \
    rpm -i /tmp/vagrant.rpm

# install Virtualbox (Example version: 5.0.14_105127_el7-1)
RUN mkdir -p /opt/virtualbox && \
    cd /etc/yum.repos.d/ && \
    curl -o virtualbox.repo http://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo && \
    yum install -y \
      dkms \
      zlib-devel \
      kernel-devel && \
    yum -y groupinstall "Development Tools" && \
    if  [ "${VIRTUALBOX_VERSION}" = "latest" ]; \
      then yum install -y VirtualBox-6.0 ; \
      else yum install -y VirtualBox-6.0-${VIRTUALBOX_VERSION} ; \
    fi && \
    yum clean all && rm -rf /var/cache/yum/* && rm -rf /tmp/*
