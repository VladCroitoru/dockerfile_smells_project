FROM node:latest

RUN apt-get -qq update \
	&& apt-get install apt-utils --assume-yes

RUN apt-get install zip --assume-yes

RUN apt-get install curl --assume-yes

RUN apt-get install ruby-dev --assume-yes \
	&& apt-get install rubygems --assume-yes \
	&& gem update --system \
	&& gem install compass \
	&& gem install dpl \
	&& gem install aws-sdk

RUN npm -g install typings --silent

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash

CMD ["node"]