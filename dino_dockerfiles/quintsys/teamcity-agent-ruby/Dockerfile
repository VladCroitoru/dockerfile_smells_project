FROM jetbrains/teamcity-minimal-agent:latest

# no docs for gems
RUN mkdir -p /etc/ \
	&& { \
		echo 'install: --no-document'; \
		echo 'update: --no-document'; \
	} >> /etc/gemrc  

# remove tty warning when executing login shells    
RUN sed -i 's/^mesg n || true$/tty -s \&\& mesg n/g' /root/.profile

# install git, rvm, nodejs and yarn
ENV RUBY_VERSION=2.4.3 \
    RUBYGEMS_VERSION=2.7.5 \
    BUNDLER_VERSION=1.16.1 

ENV SOURCE_RVM="source /usr/share/rvm/scripts/rvm" \
    RUBY_INSTALL="rvm install ${RUBY_VERSION}" \
    GEM_UPDATE="gem update --system ${RUBYGEMS_VERSION}" \
    BUNDLER_INSTALL="rvm @global do gem install bundler --version ${BUNDLER_VERSION}" \
    BUNDLER_CONFIG="bundle config --global silence_root_warning 1"

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		software-properties-common \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \   
    && apt-add-repository -y ppa:rael-gc/rvm \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        rvm \
        nodejs \ 
        yarn \
	&& rm -rf /var/lib/apt/lists/* 

# install ruby & bundler
RUN /bin/bash -c "${SOURCE_RVM} && ${RUBY_INSTALL} && ${BUNDLER_INSTALL} && ${BUNDLER_CONFIG}"

CMD /bin/bash -c "${SOURCE_RVM} && source run-services.sh"