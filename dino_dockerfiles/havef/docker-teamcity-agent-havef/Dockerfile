FROM klikatech/teamcity-agent-base

MAINTAINER Eugene Volchek <evolchek@klika-tech.com>

USER root

RUN apt-get update \
	&& apt-get install -y rsync bzip2 ruby-full build-essential ant \
		zip nodejs groff less python python-pip apt-transport-https \
	&& curl -sL https://deb.nodesource.com/setup | bash - \
	&& curl -sL https://deb.nodesource.com/setup_5.x | bash - \
	&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \
	&& apt-get update \
	&& apt-get install -y nodejs \
	&& npm install -g npm@next \
	&& npm install -g bower \
	&& npm install -g grunt-cli \
	&& npm install -g gulp-cli \
	&& gem install sass \
	&& gem install compass \
	&& gem install jekyll \
	&& curl -sSL https://get.docker.com/ | sh \
	&& apt-get -y autoremove && apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
USER teamcity
