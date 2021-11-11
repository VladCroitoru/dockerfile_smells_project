FROM mono:4.2.3.4

MAINTAINER Govind R

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install build-essential -y --no-install-recommends \
	&& apt-get install wget  -y --no-install-recommends \
	&& apt-get install curl -y \
	&& apt-get install mono-runtime -y --no-install-recommends \
    && apt-get install mono-complete fsharp -y \
	&& apt-get install nuget -y \
	&& apt-get install nunit -y \
	&& apt-get install -y git \
	&& apt-get install -y ruby-full \
	&& curl -sL https://deb.nodesource.com/setup | bash - \
	&& apt-get install nodejs -y \
	&& npm install -g grunt \
	&& npm install -g grunt-cli \
	&& gem install less \
	&& gem install sass \
	&& gem install compass \
	&& apt-get purge wget -y \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /var/tmp/* \
	&& mono --version \
	&& node --version
