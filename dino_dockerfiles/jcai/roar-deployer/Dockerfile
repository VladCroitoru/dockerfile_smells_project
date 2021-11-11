FROM alpine
MAINTAINER Jun Tsai <jcai@ganshane.com>

RUN apk add --no-cache zsh openssh-client git vim curl ruby ruby-io-console
#config sshd
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo "UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config
RUN mkdir /root/.ssh
ADD keys/id_rsa /root/.ssh/id_rsa
ADD keys/id_rsa.pub /root/.ssh/id_rsa.pub
RUN chmod 0600 /root/.ssh/id_rsa
RUN cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys

#setup capistrano
ENV BUNDLER_VERSION 1.12.5

RUN {\
  gem sources --remove http://rubygems.org/ \
    && gem sources -a https://ruby.taobao.org/ \
    && gem install bundler --version "$BUNDLER_VERSION" --no-rdoc --no-ri ;\
}


# install things globally, for great justice
# and don't create ".bundle" in all our apps
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
	BUNDLE_BIN="$GEM_HOME/bin" \
	BUNDLE_SILENCE_ROOT_WARNING=1 \
	BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
	&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"

#setup zsh
ENV HOME /root
WORKDIR /root
ENV SHELL zsh
ADD scripts/install-oh-my-zh-on-docker.sh /root/install.sh
RUN  zsh   install.sh
RUN {\
  sed -i 's/plugins=(git)/plugins=(git vi-mode history-substring-search capistrano)/g' /root/.zshrc \
  && echo "bindkey -v" >> /root/.zshrc \
  && echo "export KEYTIMEOUT=1" >> /root/.zshrc \
  && echo "bindkey -M vicmd \"k\" history-substring-search-up" >> /root/.zshrc \
  && echo "bindkey -M vicmd \"j\" history-substring-search-down" >> /root/.zshrc ;\
}
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN

WORKDIR /roar-deploy
ADD Gemfile /tmp/Gemfile
ADD Gemfile.lock /tmp/Gemfile.lock
RUN { \
  cd /tmp/  \
  && bundle install ; \
}

#setup git user
RUN git config --global user.email "jcai@ganshane.com"
RUN git config --global user.name "Jun Tsai"

ENV ROAR_USER roar
ENTRYPOINT ["zsh"]

