FROM jetbrains/teamcity-agent:10.0.3
MAINTAINER Julien Enocq <julien@enocq.fr>

ENV USER buildagent
RUN locale-gen en_US.UTF-8
ENV HOME /home/${USER}
ENV PATH ${HOME}/.rbenv/bin:$HOME/.rbenv/shims:${PATH}
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV RBENV ${HOME}/.rbenv

RUN apt-get -q update \
  && DEBIAN_FRONTEND=noninteractive apt-get -q -y --no-install-recommends install \
       wget \
       build-essential \
       libpq-dev \
       libreadline-dev \
  && apt-get -q clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN wget -O - https://github.com/sstephenson/rbenv/archive/master.tar.gz \
  | tar zxf - \
  && mv rbenv-master $HOME/.rbenv
RUN wget -O - https://github.com/sstephenson/ruby-build/archive/master.tar.gz \
  | tar zxf - \
  && mkdir -p $HOME/.rbenv/plugins \
  && mv ruby-build-master $HOME/.rbenv/plugins/ruby-build
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.profile
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc


